# 2ex-lab — ponto de retomada do projeto

**Atualizado em:** 26/11/2026  
**Finalidade:** registrar o estado de trabalho para retomar em outra conversa sem recomeçar o planejamento.

## 1. Instrução de continuidade
Continue o projeto 2ex-lab a partir deste estado. Não reinicie a estratégia nem reverta decisões anteriores. Trabalhe em português brasileiro, em etapas pequenas, gratuitas, reversíveis e de baixa manutenção. Preserve as regras editoriais e operacionais. Não publique conteúdo definitivo sem aprovação humana explícita para aquele artigo. Nunca solicitar senhas, tokens ou códigos de autenticação.

## 2. Estratégia e restrições
- Laboratório editorial independente sobre dupla excepcionalidade (2e), altas habilidades/superdotação, neurodiversidade, aprendizagem inclusiva, criatividade, IA, tecnologia assistiva e acessibilidade.
- Assinatura: “Conhecimento, experimentação e possibilidades.”
- Site único com quatro áreas: 2e Knowledge, 2e Learning, 2e Tech e 2e Resources.
- Público: famílias, educadores, pessoas neurodivergentes e profissionais interessados em aprendizagem e inclusão.
- Priorizar valor editorial e independência; monetização futura subordinada à utilidade.
- Operação: aproximadamente 4h/semana, blocos de 5–15 minutos, capital inicial zero, trabalho assíncrono e baixa manutenção.
- Não criar custos recorrentes, serviços complexos, reuniões ou atendimento individual sem justificativa e aprovação.
- Distinguir evidência, hipótese, controvérsia, experiência e opinião. Não diagnosticar, prometer resultados ou expor dados pessoais.
- Aprovação humana obrigatória antes da publicação final.

## 3. Infraestrutura confirmada
- Site: https://2ex-lab.github.io
- Repositório: https://github.com/2ex-lab/2ex-lab.github.io
- Branch: `main`; GitHub Pages + Jekyll + Minima + GitHub Actions.
- Workflows: `.github/workflows/pages.yml` (deploy) e `.github/workflows/build.yml` (build/validação).
- Páginas institucionais: início, sobre, acessibilidade e privacidade.
- Rodapé com navegação, compartilhamento nos artigos e layout de artigo implementados.
- `scripts/check_site.py` verifica estrutura HTML e elementos básicos de acessibilidade; não substitui testes manuais, leitor de tela ou auditoria WCAG completa.
- E-mail institucional e conta GitHub foram criados pelo usuário. Nunca solicitar credenciais.

## 4. Conteúdo publicado
Primeiro artigo publicado e deploy confirmado:
**Dupla excepcionalidade (2e): o que a pesquisa científica já sabe — e o que ainda não sabemos**
https://2ex-lab.github.io/2e-knowledge/dupla-excepcionalidade-o-que-a-ciencia-sabe/
O artigo foi aprovado pelo usuário. Não precisa de aprovação retroativa.

## 5. Taxonomia e Skills
Taxonomia: https://github.com/2ex-lab/2ex-lab.github.io/blob/main/.github/editorial/taxonomia.md

Cada artigo recebe uma categoria principal: `2e-knowledge`, `2e-learning`, `2e-tech` ou `2e-resources`. Usar normalmente 3–6 tags pertinentes do vocabulário controlado.

Skills no repositório:
- `.github/skills/08-escrita-cientifica-acessivel.md`
- `.github/skills/09-revisao-editorial-especialista.md`

As oito Skills originais permanecem em Markdown; não são Skills nativas instaladas automaticamente. Skill 01 — Pesquisa 2e — foi consultada e aplicada nesta retomada.

## 6. Agenda editorial
Agenda: https://github.com/2ex-lab/2ex-lab.github.io/blob/main/.github/editorial/agenda-de-publicacoes.md

Cadência inicial: duas publicações por mês, datas flexíveis:
- 08/12/2026 — 2e Knowledge: Como identificar a dupla excepcionalidade: por que nenhum teste isolado conta toda a história.
- 22/12/2026 — 2e Learning: Quando potencial e dificuldade coexistem na escola.
- 12/01/2027 — 2e Knowledge: Mascaramento na dupla excepcionalidade.
- 26/01/2027 — 2e Learning: Apoiar sem reduzir expectativas.
- 09/02/2027 — 2e Tech: IA e tecnologia assistiva no apoio à aprendizagem.
- 23/02/2027 — 2e Resources: Como avaliar um recurso educacional ou digital.

## 7. Artigo 2 — estado após segunda rodada
Título: **Como identificar a dupla excepcionalidade: por que nenhum teste isolado conta toda a história**

Rascunho (continua não público):
https://github.com/2ex-lab/2ex-lab.github.io/blob/main/_drafts/como-identificar-dupla-excepcionalidade-nenhum-teste-isolado.md

Relatório de revisão:
https://github.com/2ex-lab/2ex-lab.github.io/blob/main/.github/reviews/2026-11-26-revisao-artigo-identificacao-2e.md

Estado editorial: **aprovável após ajustes menores — pendente de aprovação humana.**

Segunda rodada consultou:
- Ozturk & Tan (2026; online first em 22/10/2025), revisão sistemática de 22 estudos: 13 utilizaram métodos formais; 9 combinaram métodos formais e informais; os autores concluem que nenhum critério isolado deve ser usado.
- Maki et al. (2026), revisão sistemática: resumo público informa que 60% dos estudos discutiram mascaramento e 7% descreveram como os procedimentos o consideraram. Texto integral restrito; o rascunho declara que usa o resumo público.
- Ogeda & Omote (2026), artigo integral SciELO sobre evidências de validade da estrutura interna da EIDEAH/TDAH versão para professores. 271 professores de uma região; modelo reduzido de 32 itens, ainda com resíduos e necessidade de estudos adicionais. Autores indicam potencial de triagem, cautela e avaliação multidisciplinar; normatização nacional não era objetivo do estudo.
- Nakano & Oliveira (2019), TIAH/S, instrumento para indicadores de AH/SD, não específico de 2e.
- Martins & Oliveira (2024), EIPIAHS-EI, instrumento de precocidade e indicadores de AH/SD na Educação Infantil, não específico de 2e.
- Fusaro et al. (2025), revisão nacional/internacional de 52 artigos empíricos, já utilizada no primeiro artigo.

A segunda rodada corrigiu a descrição da escala brasileira e distinguiu instrumentos de AH/SD de instrumentos específicos de 2e. Não houve publicação nem alteração de artigos já publicados.

Próxima ação: apresentar o rascunho atual ao usuário para leitura e aprovação humana ou ajustes. Se aprovado, somente então mover para `_posts/`, executar `scripts/check_site.py`, revisar visualmente e confirmar deploy. Se não aprovado, manter em `_drafts/`.

## 8. Automação editorial
Automação existente e confirmada como habilitada:
- Título: “Ciclo editorial 2ex-lab”
- ID: `6b085aac9f648191a9cd86a4e7830103`
- Fuso: `America/Recife`
- Próxima execução: 08/12/2026 às 15:00 (UTC−3)
- Recorrência: quinzenal às terças-feiras.
- Estado: habilitada; sem execução registrada no momento da checagem.
- Pesquisa descobertas nacionais/internacionais, consulta agenda/taxonomia/Skills 08 e 09, prepara rascunhos em `_drafts/` quando houver pauta robusta e envia alerta com fontes, link, limites e decisão humana necessária.
- Não move rascunhos para `_posts/` nem publica conteúdo final.
- Não criar automação duplicada. Alterar a existente apenas se solicitado.

## 9. Próxima sessão
1. Abrir o rascunho do artigo 2 e colher a decisão do usuário: aprovar, solicitar ajustes ou adiar.
2. Não publicar sem aprovação explícita.
3. Após aprovação, executar validação técnica, revisar o site e confirmar deploy.
4. Prosseguir para a pauta seguinte da agenda.
5. Manter a automação quinzenal e verificar execuções/alertas quando ocorrerem.

## 10. Links principais
- Site: https://2ex-lab.github.io
- Repositório: https://github.com/2ex-lab/2ex-lab.github.io
- Agenda: https://github.com/2ex-lab/2ex-lab.github.io/blob/main/.github/editorial/agenda-de-publicacoes.md
- Taxonomia: https://github.com/2ex-lab/2ex-lab.github.io/blob/main/.github/editorial/taxonomia.md
- Rascunho artigo 2: https://github.com/2ex-lab/2ex-lab.github.io/blob/main/_drafts/como-identificar-dupla-excepcionalidade-nenhum-teste-isolado.md
- Revisão artigo 2: https://github.com/2ex-lab/2ex-lab.github.io/blob/main/.github/reviews/2026-11-26-revisao-artigo-identificacao-2e.md

**Este documento é o ponto de retomada operacional.** Se houver conflito com o dossiê inicial, considerar este checkpoint e o histórico mais recente do repositório como estado atualizado, preservando a estratégia original.
