---
name: 2exlab-busca-e-correcao-sistema
description: Skill para auditar continuamente o ecossistema 2eXlab, localizar falhas e inconsistências, propor correções seguras, validar resultados e registrar evidências sem comprometer conteúdo, marca, segurança ou operação.
---

# Skill 08 — Busca e correção sistêmica

## 1. Missão

Executar uma varredura ampla, metódica e rastreável do ecossistema 2eXlab para identificar problemas, riscos, inconsistências, regressões e oportunidades de melhoria. Corrigir o que for tecnicamente seguro e estiver dentro do escopo autorizado; para mudanças sensíveis, apresentar diagnóstico e solicitar aprovação.

A Skill complementa o Orquestrador (00) e as Skills especializadas (01–07). Não substitui pesquisa científica, revisão editorial, validação jurídica, segurança profissional ou decisão do responsável pelo projeto.

**Princípio:** procurar em todo o sistema, alterar o mínimo necessário e comprovar cada correção.

## 2. Escopo da varredura

Inspecionar, conforme os recursos e permissões realmente disponíveis:

1. **Repositório e estrutura**
   - árvore de diretórios, arquivos órfãos, duplicados, nomes, extensões e organização;
   - configuração Jekyll, dependências, tema Minima, includes, layouts, data files e assets;
   - consistência entre configuração, templates, páginas e conteúdo;
   - links relativos, permalinks, rotas, âncoras e referências a arquivos inexistentes.

2. **Código, CSS e interface**
   - HTML semântico, CSS, JavaScript e Liquid;
   - regras duplicadas, conflitantes, sem uso ou excessivamente específicas;
   - responsividade, comportamento móvel, foco visível, teclado e estados interativos;
   - acessibilidade: estrutura de títulos, landmarks, rótulos, textos alternativos, contraste, áreas de toque, movimento reduzido e leitura;
   - desempenho, imagens, fontes, embeds e recursos externos.

3. **Conteúdo e taxonomia**
   - front matter, categorias, tags, datas, títulos, descrições e permalinks;
   - aderência às quatro categorias e ao vocabulário controlado do projeto;
   - consistência entre índices, páginas de categoria, tags e artigos;
   - links internos, conteúdo duplicado, páginas vazias, rascunhos expostos e metadados ausentes;
   - integridade editorial: separar evidência, hipótese, experiência e opinião; identificar alegações sem fonte, promessas indevidas e conflitos de interesse.

4. **SEO e descoberta**
   - títulos e descrições, canonical, sitemap, robots, feed, dados estruturados quando aplicáveis;
   - links quebrados, páginas órfãs, redirecionamentos, indexabilidade e hierarquia de navegação;
   - não aplicar técnicas enganosas, geração em massa ou otimização que prejudique a utilidade.

5. **Build, deploy e automação**
   - GitHub Actions, permissões dos workflows, gatilhos, versões de actions, logs e artefatos;
   - resultado de validação Jekyll e GitHub Pages;
   - divergências entre branch, commit integrado, artefato e site publicado;
   - dependências desnecessárias, avisos e falhas intermitentes.

6. **Segurança e privacidade**
   - exposição acidental de segredos, tokens, dados pessoais, informações de crianças ou arquivos indevidos;
   - permissões excessivas, dependências e scripts de terceiros;
   - políticas de privacidade, formulários, analytics e embeds sob a ótica de minimização de dados.
   - Nunca solicitar, copiar, registrar ou exibir senhas, tokens, códigos 2FA ou códigos de recuperação. Não presumir acesso às configurações privadas das contas.

7. **Marca e coerência estratégica**
   - uso consistente de 2eXlab e da assinatura “Conhecimento, experimentação e possibilidades”;
   - linguagem, identidade visual, navegação e experiência coerentes;
   - preservação do posicionamento de laboratório independente, não comercial-first;
   - compatibilidade com orçamento zero, baixa manutenção, trabalho assíncrono e disponibilidade limitada.

## 3. Limites de acesso

“Varredura de todo o sistema” significa todo o material acessível e autorizado no contexto da execução, não acesso irrestrito a contas, dispositivos ou serviços externos.

Antes de afirmar cobertura, declarar:
- repositórios, branches, diretórios, arquivos, páginas, workflows e artefatos efetivamente inspecionados;
- itens não acessíveis ou não verificados;
- data/commit/versão usados como referência;
- ferramentas e testes executados.

Não alegar auditoria completa se houve apenas busca textual, inspeção parcial ou ausência de acesso ao site publicado. Distinguir inspeção estática, build automatizado e verificação visual em navegador real.

## 4. Protocolo de execução

### Etapa A — Estabelecer a referência

1. Ler o dossiê de transferência, README, documentos de marca, operação e Skills 00–07 disponíveis.
2. Consultar o estado atual do repositório, branch principal, commits recentes, PRs abertas, workflows e deploy.
3. Identificar alterações não integradas e não sobrescrevê-las.
4. Registrar o commit-base e o escopo da auditoria.
5. Se houver documentação conflitante, preservar decisões mais recentes confirmadas no repositório e no histórico do projeto; sinalizar conflitos em vez de resolver por suposição.

### Etapa B — Descoberta ampla

1. Mapear a árvore de arquivos e configurações.
2. Examinar arquivos críticos integralmente, não apenas resultados de busca.
3. Buscar referências cruzadas, imports/includes, rotas, classes CSS, IDs, metadados e URLs.
4. Inspecionar histórico e diffs quando uma regressão ou origem provável for relevante.
5. Executar verificações automatizadas disponíveis, sem instalar serviços pagos ou dependências desnecessárias.
6. Agrupar achados relacionados para evitar correções redundantes.

### Etapa C — Registrar achados

Cada achado deve conter:
- identificador curto;
- área e arquivo/localização;
- descrição objetiva do comportamento observado;
- evidência reproduzível (trecho, linha, saída de teste, URL ou captura, quando disponível);
- impacto para pessoas usuárias ou operação;
- severidade e confiança;
- recomendação de correção;
- risco de regressão e dependências.

Classificação:
- **P0 — Crítico:** segredo exposto, risco imediato de segurança/privacidade ou perda grave de dados. Interromper publicação e orientar contenção; não apagar evidências nem rotacionar credenciais sem autorização.
- **P1 — Alto:** falha que impede build/deploy, quebra navegação essencial, expõe conteúdo privado ou compromete funcionalidade central.
- **P2 — Moderado:** acessibilidade, responsividade, conteúdo, SEO ou consistência com impacto significativo, mas com alternativa funcional.
- **P3 — Baixo:** refinamento visual, manutenção, documentação ou melhoria incremental.
- **Observação:** hipótese ou oportunidade ainda sem evidência suficiente para ser tratada como defeito.

Não inflar severidade. Separar fato confirmado de inferência.

### Etapa D — Decidir se pode corrigir

**Pode corrigir sem nova pergunta**, dentro de branch própria:
- erros objetivos e localizados;
- links internos quebrados quando o destino correto é inequívoco;
- inconsistências mecânicas de metadados quando a fonte de verdade está documentada;
- CSS e markup com defeito reproduzível, preservando identidade e comportamento;
- documentação técnica e testes que não alterem decisões estratégicas;
- correções reversíveis sem custo, exposição de dados ou impacto em terceiros.

**Exige aprovação explícita antes de executar:**
- publicar, mesclar em produção ou alterar domínio, DNS, titularidade e configurações externas;
- excluir conteúdo, repositórios, branches, histórico, dados ou recursos;
- mudar marca, posicionamento, taxonomia, arquitetura editorial ou política de monetização;
- adicionar analytics, pixels, formulários, cookies, serviços externos ou coleta de dados;
- adicionar custos, dependências com manutenção relevante, pagamentos ou integrações com permissões;
- alterar alegações científicas, recomendações sensíveis ou conteúdo que exija julgamento editorial;
- alterar permissões de conta, segurança, credenciais ou dados privados.

Se uma correção segura depender de uma decisão não documentada, não adivinhar: apresentar opções e perguntar somente o necessário.

### Etapa E — Implementar com segurança

1. Nunca editar diretamente `main` como fluxo normal.
2. Criar branch com nome descritivo a partir do commit-base confirmado.
3. Fazer mudanças pequenas, coesas e mínimas.
4. Preservar conteúdo existente, URLs, slugs, categorias, tags e identidade visual, salvo autorização específica.
5. Não reformatar arquivos inteiros por conveniência quando uma alteração pontual resolve.
6. Não incluir segredos, dados pessoais ou arquivos de build no commit.
7. Atualizar documentação e testes quando a correção alterar comportamento.
8. Criar PR com contexto, problema, solução, arquivos afetados, riscos, testes e itens não verificados.
9. Não mesclar a PR sem autorização explícita do usuário. A autorização para corrigir ou abrir PR não equivale à autorização para publicar.

### Etapa F — Validar a correção

Executar, conforme aplicável:
- validação YAML/front matter e estrutura;
- build Jekyll em ambiente compatível;
- verificações de links, rotas, âncoras e arquivos;
- testes de CSS/HTML e busca por seletores órfãos;
- revisão de contraste WCAG para texto normal e grande, sem inferir acessibilidade total a partir de contraste;
- inspeção de responsividade em larguras representativas;
- navegação por teclado e foco;
- inspeção de logs e conclusão dos workflows;
- comparação do artefato gerado com o commit esperado;
- verificação visual real do site publicado, quando navegador estiver disponível.

Não afirmar que um teste passou se ele não foi executado. Registrar limitações, avisos e falhas remanescentes. Se uma validação falhar, investigar e corrigir na mesma branch antes de pedir revisão, quando seguro.

### Etapa G — Fechar o ciclo

Entregar um resumo curto e verificável:
- escopo efetivamente auditado;
- quantidade e severidade dos achados;
- correções feitas e arquivos alterados;
- testes executados e resultados;
- PR e commit;
- riscos ou itens pendentes;
- decisão que depende do usuário.

Manter um backlog de achados não corrigidos, com motivo e prioridade, sem transformar toda observação em tarefa imediata.

## 5. Critérios de qualidade específicos do 2eXlab

- Não sacrificar legibilidade ou acessibilidade por estética.
- Não introduzir frameworks ou serviços pagos quando CSS, Jekyll ou recursos nativos resolvem.
- Não criar sites separados para as quatro áreas editoriais.
- Manter as categorias internas `knowledge`, `learning`, `tech`, `resources` e seus rótulos públicos documentados.
- Usar a taxonomia controlada existente; não inventar tags por artigo.
- Não criar páginas SEO vazias para tags sem conteúdo.
- Preservar URLs públicas já estabelecidas.
- Tratar recomendações e afiliados com transparência.
- Não diagnosticar, prometer resultados nem expor crianças identificáveis.
- Preferir mudanças pequenas, gratuitas, reversíveis e de baixa manutenção.

## 6. Comando de ativação

Quando acionada com “varra o sistema”, “audite tudo”, “procure e corrija”, “faça uma revisão geral” ou equivalente:

1. estabelecer a referência atual;
2. executar a descoberta ampla por áreas;
3. registrar achados com evidências e severidade;
4. corrigir automaticamente apenas o que estiver dentro dos limites autorizados;
5. abrir PRs coesas, preferencialmente uma por grupo de mudanças;
6. aguardar autorização para merge/publicação;
7. apresentar o relatório e o backlog.

Se o usuário pedir correção imediata e já tiver autorizado integração, essa autorização pode ser aplicada às PRs cobertas pelo pedido atual, desde que a validação esteja aprovada e não haja mudança sensível. Não estender autorização a ações futuras ou a alterações de natureza diferente.

## 7. Formato mínimo do relatório

| Campo | Conteúdo |
|---|---|
| Referência | commit, branch e data |
| Cobertura | áreas e arquivos inspecionados |
| Limitações | o que não foi possível verificar |
| Achados | ID, severidade, evidência e impacto |
| Correções | arquivos e resumo das mudanças |
| Validação | comandos/testes e resultados |
| Integração | PR, estado e commit |
| Pendências | decisão, risco ou ação futura |

**Regra final:** uma auditoria útil não é a que promete encontrar tudo; é a que deixa claro o que foi examinado, o que foi encontrado, o que foi corrigido e o que ainda não pode ser afirmado.
