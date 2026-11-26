#!/usr/bin/env python3
"""Dependency-free structural UX/accessibility checks for the built Jekyll site, including control labels."""
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
        self._labels_for = set()
        self._controls = []
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
            if a.get("for"):
                self._labels_for.add(a["for"])
        if tag in ("input", "select", "textarea", "button"):
            control_type = a.get("type", "").lower()
            if tag != "input" or control_type != "hidden":
                initial_text = a.get("value", "") if tag == "input" and control_type in ("submit", "button", "reset") else a.get("alt", "") if tag == "input" and control_type == "image" else ""
                control = {
                    "tag": tag,
                    "type": control_type,
                    "id": a.get("id", ""),
                    "aria_label": a.get("aria-label", "").strip(),
                    "aria_labelledby": a.get("aria-labelledby", "").split(),
                    "wrapped_by_label": self._label_depth > 0,
                    "text": initial_text,
                }
                self._controls.append(control)
                if tag == "button":
                    self._current_control = control

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "label" and self._label_depth:
            self._label_depth -= 1
        elif tag == "a":
            self._link = None
        elif tag == "button":
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
    control_ids = {control["id"] for control in parser._controls if control["id"]}
    for control in parser._controls:
        labelled_by_valid = bool(control["aria_labelledby"]) and all(ref in parser.ids for ref in control["aria_labelledby"])
        associated_label = bool(control["id"]) and control["id"] in parser._labels_for
        button_text = control["tag"] == "button" and bool(control["text"].strip())
        input_value = control["tag"] == "input" and control["type"] in ("submit", "button", "reset", "image") and bool(control["text"].strip())
        if not (control["aria_label"] or labelled_by_valid or associated_label or control["wrapped_by_label"] or button_text or input_value):
            parser.controls_without_name += 1
    for label_target in parser._labels_for:
        if label_target not in control_ids:
            errors.append(f"{rel}: label associado a controle inexistente: {label_target}")
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
print("Aprovação estrutural: idioma, viewport, título, H1, landmarks, imagens, rótulos de controles, IDs, hierarquia e links internos.")
