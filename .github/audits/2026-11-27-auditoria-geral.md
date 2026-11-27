# Auditoria do site 2ex-lab — 27/11/2026

## Referência

- Repositório: https://github.com/2ex-lab/2ex-lab.github.io
- Branch-base: `main`
- Commit-base: `4c79ef08cec09ff2cf39a785306fa8158c787ee2`
- Branch de correção: `audit/2026-11-27-site-review`
- Stack identificada: GitHub Pages, Jekyll, tema Minima, GitHub Actions.
- Skill aplicada: `.github/skills/10-auditoria-busca-correcao-zeladoria.md`.

## Objetivo e critério

Inspecionar o material do repositório acessível, procurar inconsistências técnicas e editoriais com evidência, corrigir somente problemas objetivos e reversíveis e preservar conteúdo, URLs, identidade e histórico. As alterações foram preparadas em branch separada; não foram integradas à `main` nem publicadas.

## Cobertura realizada

Inspeção estática dos seguintes componentes:

- configuração e dependências: `_config.yml`, `Gemfile`;
- workflows: `.github/workflows/build.yml`, `.github/workflows/pages.yml`;
- templates e navegação: `_layouts/default.html`, `_includes/head.html`, `_includes/header.html`, `_includes/footer.html`, `_includes/share-links.html`;
- CSS e verificador: `assets/css/custom.css`, `scripts/check_site.py`;
- páginas: início, sobre, categorias, acessibilidade, privacidade, índice de tags e quatro páginas de área;
- taxonomia: `_data/taxonomy.yml` e documentação editorial;
- conteúdo: os dois artigos atualmente publicados;
- operação: README, agenda, ponto de retomada anterior e Skill 10;
- histórico recente, incluindo a reversão das preferências de leitura no commit-base.

## Achados e correções preparadas

### AUD-01 — Canal de contato contraditório
- **Severidade:** P2 — moderada.
- **Evidência:** `_config.yml` define o e-mail institucional e `_includes/footer.html` o apresenta publicamente. Em contraste, `sobre.md` dizia que os canais de contato ainda seriam informados e `acessibilidade.md` afirmava que não havia canal público.
- **Impacto:** informação contraditória para quem precisa entrar em contato ou relatar uma barreira de acessibilidade.
- **Correção preparada:** as duas páginas agora orientam a pessoa a usar o e-mail do rodapé, explicam os limites do atendimento e pedem que não sejam enviados dados pessoais ou sensíveis.

### AUD-02 — Agenda e README desatualizados
- **Severidade:** P3 — baixa.
- **Evidência:** o artigo “Como identificar a dupla excepcionalidade...” foi publicado no commit `233286babb1e5eb7f2eba4624a35992c149af6e4` em 26/11/2026, mas a agenda ainda o apresentava como pauta futura para 08/12/2026. O README ainda instruía obter aprovação de um rascunho que já havia sido publicado e removido de `_drafts/`.
- **Impacto:** instruções de continuidade incorretas e risco de duplicar uma pauta.
- **Correção preparada:** a agenda registra a publicação antecipada; o README lista os dois artigos publicados e aponta a pauta de 22/12/2026 como próxima etapa.

### AUD-03 — Divergência de escopo entre documentos
- **Severidade:** Observação estratégica — requer decisão humana.
- **Evidência:** o repositório e o site implementam um laboratório editorial sobre dupla excepcionalidade. O documento-fonte estratégico de 27/11/2026 descreve um negócio baseado em IA e entregáveis delimitados, com produto e público ainda não definidos.
- **Impacto:** risco de orientar futuras mudanças de site, marca, conteúdo ou aquisição com base em premissas incompatíveis.
- **Tratamento:** não alterado. A decisão de manter, separar, reaproveitar ou reformular o site exige confirmação explícita.

## Revisão técnica estática

- A configuração aponta para Jekyll/Minima e carrega os plugins `jekyll-feed` e `jekyll-seo-tag`.
- Os workflows separam validação de build e publicação do GitHub Pages; o workflow de publicação só publica a partir de `main` ou por execução manual.
- A navegação móvel usa o elemento nativo `details/summary`, sem exigir JavaScript.
- Há link para pular ao conteúdo, idioma `pt-BR`, viewport, landmark principal, foco visível e regra para movimento reduzido.
- O verificador `scripts/check_site.py` examina HTML gerado, títulos, H1, landmarks, IDs, imagens sem atributo alt, nomes acessíveis de controles, hierarquia de títulos e links internos. Ele não substitui teste manual, leitores de tela ou auditoria WCAG completa.
- A inspeção não confirmou erro funcional de código que justificasse alterar templates, CSS ou workflows. Não foram feitas refatorações especulativas.

## Limitações da auditoria

- A conexão disponível permitiu ler arquivos específicos, mas não forneceu inventário completo da árvore do repositório. Portanto, não é correto afirmar que todos os arquivos e diretórios foram inspecionados.
- Não foi possível executar `bundle exec jekyll build` nem `python3 scripts/check_site.py` neste ambiente.
- A tentativa de abrir o site publicado pelo navegador de pesquisa não foi bem-sucedida; não houve inspeção visual real em desktop ou celular.
- O status agregado consultado para o commit-base não retornou verificações. Isso não comprova aprovação nem reprovação de build.
- Links externos, contraste calculado, experiência com leitor de tela, Core Web Vitals, sitemap/robots gerados e configurações privadas do GitHub Pages não foram verificados.
- A ausência de arquivos-fonte `sitemap.xml` e `robots.txt` no caminho consultado não permite concluir que esses recursos estejam ausentes do artefato publicado.

## Arquivos alterados nesta proposta

- `sobre.md`
- `acessibilidade.md`
- `README.md`
- `.github/editorial/agenda-de-publicacoes.md`

Nenhum artigo publicado, rascunho, arquivo de taxonomia, configuração de deploy, CSS, JavaScript ou histórico foi alterado.

## Validação e integração

- Pull Request: [#17 — Auditoria do site: corrige contato e estado editorial](https://github.com/2ex-lab/2ex-lab.github.io/pull/17).
- Revisão estática dos arquivos alterados: concluída.
- Build Jekyll e verificador estrutural: ainda sem resultado visível pela conexão no momento do registro; não declarar aprovação.
- Inspeção visual do site publicado: pendente.
- Merge em `main` e publicação: não realizados.

## Próximas decisões

1. Aguardar o resultado do workflow de validação da Pull Request.
2. Revisar e aprovar a proposta antes de qualquer merge.
3. Decidir separadamente qual é o escopo futuro do site diante da divergência estratégica registrada em AUD-03.
