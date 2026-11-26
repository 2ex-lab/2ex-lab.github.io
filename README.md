# 2ex-lab

**Conhecimento, experimentação e possibilidades.**

Laboratório independente de conhecimento e experimentação sobre dupla excepcionalidade (2e), altas habilidades/superdotação, neurodiversidade, aprendizagem, educação inclusiva, criatividade, tecnologia, inteligência artificial e acessibilidade.

## Estado do projeto

O site está publicado no GitHub Pages: https://2ex-lab.github.io.

A publicação é automatizada pelo workflow `.github/workflows/pages.yml`, acionado por atualizações na branch `main` e também manualmente (`workflow_dispatch`). O workflow compila o site com Jekyll, executa verificações estruturais de UX e acessibilidade e publica o artefato no GitHub Pages.

O workflow `.github/workflows/build.yml` realiza validações de compilação e estrutura em eventos de integração, sem executar a publicação.

A versão pública atual é uma estrutura institucional inicial. As quatro áreas editoriais estão em preparação; seus conteúdos serão incluídos após pesquisa e revisão humana. A aprovação de publicação do site não significa aprovação automática de artigos ou recomendações futuras.

## Áreas editoriais

- **2e Knowledge** — ciência, conceitos e pesquisas.
- **2e Learning** — educação, aprendizagem, família e inclusão.
- **2e Tech** — IA, tecnologia assistiva, acessibilidade e ferramentas.
- **2e Resources** — guias, materiais, bibliotecas e comparativos.

O site é um único projeto editorial, não quatro sites separados.

## Princípios

- Priorizar conhecimento, experimentação e utilidade pública.
- Distinguir evidências, hipóteses, controvérsias, experiências e opiniões.
- Valorizar acessibilidade, privacidade e transparência.
- Preferir soluções simples, gratuitas, reversíveis e de baixa manutenção.
- Não diagnosticar, prescrever ou prometer resultados.
- Não publicar conteúdo editorial definitivo sem revisão humana.

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

## Próximas etapas

1. Concluir a auditoria pública: páginas, links, navegação móvel, HTTPS, `robots.txt` e `sitemap.xml`.
2. Registrar e tratar eventuais barreiras de acessibilidade que não sejam cobertas pelas verificações automatizadas.
3. Manter as páginas institucionais e a documentação coerentes com o estado efetivo do site.
4. Planejar os primeiros conteúdos editoriais seguindo os critérios de pesquisa, revisão humana e transparência do projeto.
