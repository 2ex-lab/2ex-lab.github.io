# 2ex-lab

**Conhecimento, experimentação e possibilidades.**

Laboratório independente de conhecimento e experimentação sobre dupla excepcionalidade (2e), altas habilidades/superdotação, neurodiversidade, aprendizagem, educação inclusiva, criatividade, tecnologia, inteligência artificial e acessibilidade.

## Estado do projeto

O site está publicado no GitHub Pages: https://2ex-lab.github.io.

Esta branch contém um **protótipo de avaliação do tema Basically Basic 1.4.5**. A experiência não está aprovada para publicação; a branch `main` permanece como versão publicada até decisão posterior.

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

GitHub + GitHub Pages + Jekyll + GitHub Actions + Basically Basic (em avaliação nesta branch).

- O tema é carregado por `remote_theme`, fixado na versão 1.4.5.
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

As Skills operacionais e editoriais ficam em `.github/skills/` e são documentos Markdown versionados; não são Skills nativas instaladas automaticamente no ChatGPT. Os pontos de continuidade, a agenda editorial e as auditorias ficam em `.github/editorial/` e `.github/audits/`.

## Próximas etapas

1. Preparar e revisar a pauta de **2e Learning** prevista para 22/12/2026: barreiras, apoios e participação quando potencial e dificuldade coexistem na escola.
2. Manter a cadência de duas publicações mensais, com datas flexíveis e aprovação humana explícita antes de cada publicação.
3. Avaliar o protótipo do tema em desktop e celular antes de decidir sobre sua adoção.
4. Manter decisões editoriais e estratégicas alinhadas às orientações atuais do projeto.

## Conteúdos publicados

- [Dupla excepcionalidade (2e): o que a pesquisa científica já sabe — e o que ainda não sabemos](https://2ex-lab.github.io/2e-knowledge/dupla-excepcionalidade-o-que-a-ciencia-sabe/).
- [Como identificar a dupla excepcionalidade: por que nenhum teste isolado conta toda a história](https://2ex-lab.github.io/2e-knowledge/como-identificar-dupla-excepcionalidade/).
- [Quando potencial e dificuldade coexistem na escola: barreiras, apoios e participação](https://2ex-lab.github.io/2e-learning/dupla-excepcionalidade-escola-barreiras-apoios-participacao/).
