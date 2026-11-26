---
name: 2exlab-auditoria-e-zeladoria-sistema
description: Skill para auditar continuamente o ecossistema 2eXlab, localizar falhas e inconsistências, propor correções seguras, validar resultados e registrar evidências sem comprometer conteúdo, marca, segurança ou operação.
---

# Skill 10 — Auditoria, busca, correção e zeladoria sistêmica

## 1. Missão

Executar uma varredura ampla, metódica e rastreável do ecossistema 2eXlab para identificar problemas, riscos, inconsistências, regressões e oportunidades de melhoria. Corrigir o que for tecnicamente seguro e estiver dentro do escopo autorizado; para mudanças sensíveis, apresentar diagnóstico e solicitar aprovação.

A Skill complementa o Orquestrador (00), as Skills especializadas (01–07) e as Skills editoriais 08 e 09 mantidas em `.github/skills/`. Não substitui pesquisa científica, revisão editorial, validação jurídica, segurança profissional ou decisão do responsável pelo projeto.

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


## 8. Limpeza, organização e otimização contínuas (“recolher o lixo”)

A Skill também deve atuar como zeladora técnica do ecossistema: identificar resíduos digitais, reduzir redundâncias, simplificar a estrutura e melhorar desempenho e manutenção. A limpeza não é apenas apontar problemas: quando o item for comprovadamente descartável, reversível e estiver dentro das permissões, a Skill deve preparar e executar a remoção em branch, validar e documentar.

### 8.1 O que procurar

- arquivos temporários, caches, logs locais, arquivos de editor/IDE e sistema operacional sem função no projeto;
- artefatos de build, pastas de dependências vendorizadas ou saídas geradas que não devam ser versionadas;
- imagens, fontes, documentos e scripts duplicados ou sem referências;
- CSS, JavaScript, includes, layouts, snippets, variáveis e dependências sem uso;
- páginas, rascunhos, anexos e cópias antigas redundantes;
- comentários obsoletos, código morto, regras substituídas e configurações repetidas;
- workflows redundantes, etapas repetidas, permissões excessivas e execuções desnecessárias;
- links, redirecionamentos e referências quebradas após mudanças anteriores;
- arquivos excessivamente grandes, imagens pesadas, formatos ineficientes e recursos carregados sem necessidade;
- dívida técnica, complexidade acidental, sobreposição de responsabilidades e documentação desatualizada.

### 8.2 Classificação antes de limpar

Classificar cada candidato como:

1. **Lixo comprovado:** temporário ou gerado, recriável, sem referência funcional e explicitamente fora do versionamento esperado.
2. **Redundância comprovada:** cópia idêntica ou recurso substituído, com dependências e referências verificadas.
3. **Possível obsoleto:** sem uso aparente, mas com finalidade incerta, histórico relevante ou referência indireta.
4. **Ativo necessário:** arquivo ou recurso em uso, fonte de verdade, histórico, backup ou material de referência.

Só os grupos 1 e 2 podem ser removidos automaticamente, e apenas em branch, após confirmar escopo, referências, histórico e possibilidade de restauração. Grupos 3 e 4 não devem ser removidos sem aprovação explícita.

### 8.3 Rotina de limpeza segura

1. Inventariar antes de apagar: caminho, tipo, tamanho, data/última alteração quando disponível e referências encontradas.
2. Confirmar se o arquivo é gerado, temporário, duplicado ou substituível; não inferir obsolescência apenas pela idade ou ausência de referência textual.
3. Procurar referências explícitas e indiretas em configurações, Liquid, Markdown, HTML, CSS, JavaScript, workflows, links e histórico Git.
4. Preservar fontes originais, conteúdo editorial, documentos de marca, Skills, dados de taxonomia e histórico de decisões.
5. Preferir remoção pequena e agrupada por tipo; não combinar limpeza ampla com refatoração funcional.
6. Manter a possibilidade de restauração via Git e registrar a lista de caminhos removidos.
7. Atualizar .gitignore apenas para padrões de resíduos comprovados; não ignorar genericamente arquivos que possam ser fontes.
8. Se o item for necessário para auditoria ou rastreabilidade, arquivar ou documentar em vez de apagar — e pedir aprovação se isso alterar a organização ou disponibilidade.
9. Nunca apagar branches, tags, releases, issues, PRs, histórico Git, backups, contas, repositórios, conteúdo publicado ou dados do usuário como “limpeza automática”.
10. Nunca executar limpeza destrutiva em produção, contas externas ou dispositivos; limitar-se ao repositório e ambientes explicitamente acessíveis.

### 8.4 Otimização sem excesso de engenharia

Priorizar, nesta ordem:

- **Impacto para pessoas:** legibilidade, acessibilidade, navegação, estabilidade e tempo de carregamento.
- **Simplicidade:** remover duplicação real, reduzir etapas e manter uma única fonte de verdade.
- **Desempenho:** otimizar imagens e recursos, reduzir CSS/JS desnecessário, evitar chamadas externas e carregamento prematuro.
- **Manutenção:** reduzir dependências, automações frágeis, configurações repetidas e instruções contraditórias.
- **Custo operacional:** preferir soluções nativas, gratuitas, assíncronas e de baixa manutenção.

Toda otimização deve declarar o benefício esperado e como será medido. Não fazer micro-otimizações sem impacto demonstrável, não adicionar ferramentas pesadas para medir um site pequeno e não trocar uma solução simples por arquitetura mais complexa sem justificativa.

### 8.5 Portões de segurança para exclusão

A autorização para “limpar”, “recolher o lixo” ou “otimizar” permite remover apenas resíduos técnicos comprovados e recriáveis no repositório, em branch, com diff revisável e testes. Não significa autorização genérica para excluir material de valor incerto.

Exigem confirmação específica:
- apagar conteúdo editorial, rascunhos, imagens ou documentos cuja finalidade não esteja comprovadamente encerrada;
- remover versões antigas, backups, arquivos históricos ou materiais de referência;
- excluir dependências ou componentes com uso indireto ou não testado;
- apagar branches, tags, releases, issues, PRs ou commits;
- alterar URLs públicas, eliminar páginas, consolidar conteúdos ou criar redirecionamentos;
- alterar configurações de conta, permissões, dados, serviços ou recursos externos.

Em caso de dúvida, manter e reportar. A economia de alguns bytes nunca justifica perder conhecimento, histórico, acessibilidade ou continuidade.

### 8.6 Resultado esperado da limpeza

O relatório deve incluir:
- inventário do que foi analisado;
- itens removidos, motivo e caminhos;
- redundâncias consolidadas e referências atualizadas;
- dependências e código morto removidos;
- ganhos medidos (por exemplo, redução de tamanho do artefato, número de assets, dependências ou etapas), quando possível;
- verificações de links, build, acessibilidade e regressão;
- itens suspeitos preservados e motivo pelo qual aguardam decisão.

**Regra de zeladoria:** deixar o sistema menor, mais claro, mais rápido e mais fácil de manter — sem apagar contexto, comprometer funções ou transformar limpeza em reescrita.
