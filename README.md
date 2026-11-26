# 2ex-lab

**Conhecimento, experimentação e possibilidades.**

Laboratório independente de conhecimento e experimentação sobre dupla excepcionalidade (2e), altas habilidades/superdotação, neurodiversidade, aprendizagem, educação inclusiva, criatividade, tecnologia, inteligência artificial e acessibilidade.

## Estado do projeto

O site está publicado no GitHub Pages: https://2ex-lab.github.io.

A publicação é automatizada pelo workflow `.github/workflows/pages.yml`, acionado por atualizações na branch `main` e também manualmente (`workflow_dispatch`). O workflow compila o site com Jekyll, executa verificações estruturais de UX e acessibilidade e publica o artefato no GitHub Pages.

O workflow `.github/workflows/build.yml` realiza validações de compilação e estrutura em eventos de integração, sem executar a publicação.

O primeiro artigo de 2e Knowledge já foi publicado após revisão editorial assistida e aprovação humana. As demais áreas editoriais avançarão conforme pesquisa, revisão e capacidade operacional. A aprovação de publicação de um artigo não implica aprovação automática de conteúdos futuros.

## Áreas editoriais

- **2e Knowledge** — ciência, conceitos e pesquisas.
- **2e Learning** — educação, aprendizagem, família e inclusão.
- **2e Tech** — IA, tecnologia assistiva, acessibilidade e ferramentas.
- **2e Resources** — guias, materiais, bibliotecas e comparativos.

O site é um único projeto editorial, não quatro sites separados.

## Taxonomia editorial

A classificação editorial usa quatro categorias principais correspondentes às áreas do site (`2e-knowledge`, `2e-learning`, `2e-tech` e `2e-resources`) e um vocabulário controlado de tags transversais. A referência oficial, com critérios de atribuição e governança, está em [`.github/editorial/taxonomia.md`](.github/editorial/taxonomia.md). Cada artigo recebe uma categoria principal e apenas tags materialmente pertinentes.

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
