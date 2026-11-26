# 2ex-lab

**Conhecimento, experimentação e possibilidades.**

Laboratório independente de conhecimento e experimentação sobre dupla excepcionalidade (2e), altas habilidades/superdotação, neurodiversidade, aprendizagem, educação inclusiva, criatividade, tecnologia, inteligência artificial e acessibilidade.

## Estado do projeto

O site está publicado no GitHub Pages: https://2ex-lab.github.io.

A publicação é automatizada pelo workflow `.github/workflows/pages.yml`, acionado por atualizações na branch `main` e também manualmente (`workflow_dispatch`). O workflow compila o site com Jekyll, executa verificações estruturais de UX e acessibilidade e publica o artefato no GitHub Pages.

O workflow `.github/workflows/build.yml` realiza validações de compilação e estrutura em eventos de integração, sem executar a publicação.

## Áreas editoriais

- **2e Knowledge** — ciência, conceitos e pesquisas.
- **2e Learning** — educação, aprendizagem, família e inclusão.
- **2e Tech** — IA, tecnologia assistiva, acessibilidade e ferramentas.
- **2e Resources** — guias, materiais, bibliotecas e comparativos.

O site é um único projeto editorial, não quatro sites separados.

## Taxonomia editorial implementada

A taxonomia utiliza quatro categorias internas (`knowledge`, `learning`, `tech`, `resources`), apresentadas publicamente como as quatro áreas editoriais acima, e um vocabulário controlado de 36 tags transversais. A fonte estruturada está em `_data/taxonomy.yml`; a referência editorial e as regras de atribuição estão em [`.github/editorial/taxonomia.md`](.github/editorial/taxonomia.md). O [índice de tags](/tags/) apresenta os assuntos e os conteúdos associados. As páginas de área listam automaticamente os artigos publicados na respectiva categoria.

Cada artigo recebe uma categoria principal e somente tags materialmente pertinentes. Os cinco pilares editoriais são metadados transversais, não categorias.

## Tecnologia

GitHub + GitHub Pages + Jekyll + GitHub Actions.

- `.github/workflows/build.yml`: validação de compilação e verificações estruturais.
- `.github/workflows/pages.yml`: compilação, verificações estruturais e publicação no GitHub Pages.

## Desenvolvimento local

Requisitos: Ruby e Bundler.

```bash
bundle install
bundle exec jekyll serve
```

Acesse `http://localhost:4000`.

## Skills e documentação operacional

As Skills operacionais e editoriais ficam em `.github/skills/` e são documentos Markdown versionados; não são Skills nativas instaladas automaticamente no ChatGPT. O ponto de retomada do projeto está em `.github/editorial/ponto-de-retomada-2026-11-26.md`.

## Próximas etapas

1. Obter a decisão humana sobre o rascunho do segundo artigo, mantendo-o em `_drafts/` até aprovação explícita.
2. Manter o ciclo editorial quinzenal e a agenda flexível, sem publicação automática.
3. Continuar a auditoria técnica e a zeladoria do repositório com a Skill 10, registrando evidências e preservando conteúdo e histórico.
4. Conferir build, verificações estruturais e deploy após mudanças integradas.
