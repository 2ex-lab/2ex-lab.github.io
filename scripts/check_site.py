#!/usr/bin/env python3
"""Lightweight, dependency-free structural UX/accessibility checks for the built Jekyll site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import sys

ROOT = Path("_site")
errors = []
checked_pages = 0

class PageAudit(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.html_lang = None
        self.viewport = False
        self.title = ""
        self.in_title = False
        self.h1_count = 0
        self.heading_levels = []
        self.main_count = 0
        self.nav_count = 0
        self.ids = set()
        self.duplicate_ids = set()
        self.links = []
        self.images_without_alt = 0
        self.controls_without_name = 0
        self._link = None
        self._label_depth = 0
        self._labelled_controls = set()
        self._current_control = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.html_lang = a.get("lang")
        elif tag == "meta" and a.get("name", "").lower() == "viewport":
            self.viewport = True
        elif tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.heading_levels.append(int(tag[1]))
        elif tag == "main":
            self.main_count += 1
        elif tag == "nav":
            self.nav_count += 1
        if "id" in a:
            if a["id"] in self.ids:
                self.duplicate_ids.add(a["id"])
            self.ids.add(a["id"])
        if tag == "a":
            self._link = {"href": a.get("href", ""), "text": "", "label": a.get("aria-label", "")}
            self.links.append(self._link)
        if tag == "img" and "alt" not in a:
            self.images_without_alt += 1
        if tag == "label":
            self._label_depth += 1
        if tag in ("input", "select", "textarea", "button"):
            if tag == "button":
                self._current_control = {"tag": tag, "label": a.get("aria-label", ""), "text": ""}
            elif a.get("type", "").lower() not in ("hidden", "submit", "button", "reset"):
                name = a.get("id") or a.get("name")
                if not a.get("aria-label") and not a.get("aria-labelledby") and not name:
                    self.controls_without_name += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "label" and self._label_depth:
            self._label_depth -= 1
        elif tag == "a":
            self._link = None
        elif tag == "button":
            if self._current_control and not (self._current_control["label"] or self._current_control["text"].strip()):
                self.controls_without_name += 1
            self._current_control = None

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self._link is not None:
            self._link["text"] += data
        if self._current_control is not None:
            self._current_control["text"] += data

def audit(path):
    global checked_pages
    parser = PageAudit()
    try:
        parser.feed(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path}: HTML não pôde ser analisado: {exc}")
        return
    checked_pages += 1
    rel = path.relative_to(ROOT)
    if not parser.html_lang:
        errors.append(f"{rel}: atributo lang ausente em <html>")
    if not parser.viewport:
        errors.append(f"{rel}: meta viewport ausente")
    if not parser.title.strip():
        errors.append(f"{rel}: <title> vazio ou ausente")
    if parser.h1_count != 1:
        errors.append(f"{rel}: esperado exatamente um <h1>; encontrado {parser.h1_count}")
    if parser.main_count != 1:
        errors.append(f"{rel}: esperado exatamente um landmark <main>; encontrado {parser.main_count}")
    if parser.nav_count < 1:
        errors.append(f"{rel}: landmark <nav> não encontrado")
    if parser.images_without_alt:
        errors.append(f"{rel}: {parser.images_without_alt} imagem(ns) sem atributo alt")
    if parser.controls_without_name:
        errors.append(f"{rel}: {parser.controls_without_name} controle(s) sem nome acessível")
    if parser.duplicate_ids:
        errors.append(f"{rel}: IDs duplicados: {', '.join(sorted(parser.duplicate_ids))}")
    previous = 0
    for level in parser.heading_levels:
        if previous and level > previous + 1:
            errors.append(f"{rel}: salto de hierarquia de títulos h{previous} para h{level}")
            break
        previous = level
    for link in parser.links:
        href = link["href"].strip()
        if not href:
            errors.append(f"{rel}: link <a> sem href")
            continue
        if not (link["text"].strip() or link["label"].strip()):
            errors.append(f"{rel}: link sem texto ou aria-label: {href}")
        parsed = urlparse(href)
        if parsed.scheme or parsed.netloc or href.startswith("#"):
            if href.startswith("#") and href[1:] and unquote(parsed.fragment) not in parser.ids:
                errors.append(f"{rel}: âncora interna inexistente: {href}")
            continue
        target_path = unquote(parsed.path)
        if not target_path:
            target = path
        else:
            target = ROOT / target_path.lstrip("/") if target_path.startswith("/") else (path.parent / target_path)
        if target.is_dir():
            target = target / "index.html"
        elif not target.suffix:
            target = target / "index.html"
        if not target.exists():
            errors.append(f"{rel}: destino interno inexistente: {href}")
        elif parsed.fragment and target.suffix == ".html":
            target_parser = PageAudit()
            try:
                target_parser.feed(target.read_text(encoding="utf-8"))
                if unquote(parsed.fragment) not in target_parser.ids:
                    errors.append(f"{rel}: fragmento não encontrado em {href}")
            except Exception:
                pass

if not ROOT.exists():
    print("ERRO: diretório _site não encontrado. Execute o Jekyll antes.")
    sys.exit(2)

for html in sorted(ROOT.rglob("*.html")):
    audit(html)

print(f"Páginas HTML verificadas: {checked_pages}")
if errors:
    print(f"Problemas encontrados: {len(errors)}")
    for error in errors:
        print(f" - {error}")
    sys.exit(1)
print("Aprovação estrutural: idioma, viewport, título, H1, landmarks, imagens, controles, IDs, hierarquia e links internos.")
