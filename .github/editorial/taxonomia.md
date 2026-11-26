# Taxonomia editorial do 2ex-lab

**Status:** vocabulário controlado inicial, versão 1.0  
**Escopo:** site, artigos, páginas de área, pautas, metadados, pesquisa, revisão e descoberta.  
**Princípio:** uma taxonomia pequena e consistente é melhor que tags numerosas, redundantes ou criadas apenas para SEO.

## 1. Modelo conceitual

A organização editorial tem três níveis complementares:

1. **Pilares estratégicos** — organizam o equilíbrio de temas e a intenção editorial.
2. **Áreas editoriais** — categorias principais de navegação e classificação dos conteúdos no Jekyll.
3. **Assuntos transversais** — tags controladas que descrevem conceitos, públicos, condições, práticas e formatos presentes em cada conteúdo.

Pilares e áreas não são sinônimos. Os pilares orientam o planejamento; as áreas organizam a publicação. Um artigo recebe uma única categoria principal, ainda que dialogue com vários pilares.

## 2. Pilares estratégicos

Os percentuais abaixo são hipóteses de planejamento, não cotas rígidas:

| Pilar | Peso inicial | Abrangência |
|---|---:|---|
| Dupla excepcionalidade e altas habilidades | 40% | conceitos, perfis, evidências, identificação e desenvolvimento de potencial |
| Família, escola e inclusão | 35% | aprendizagem, práticas educativas, participação, acessibilidade pedagógica e apoio |
| Tecnologia assistiva e acessibilidade | 25% | IA, ferramentas, tecnologias, acessibilidade digital e experimentação |

A distribuição pode mudar com a evolução do projeto, interesse editorial e evidências de utilidade para o público.

## 3. Categorias principais — áreas editoriais

Todo artigo publicado deve receber **exatamente uma** das categorias abaixo, em minúsculas e com hífen. A categoria deve refletir a finalidade principal do artigo, não todos os assuntos mencionados.

| Categoria Jekyll | Área | Incluir quando o foco principal for |
|---|---|---|
| `2e-knowledge` | 2e Knowledge | ciência, conceitos, terminologia, pesquisas, legislação, evidências, identificação e limites do conhecimento |
| `2e-learning` | 2e Learning | aprendizagem, família, escola, educação, práticas inclusivas, participação e apoio pedagógico |
| `2e-tech` | 2e Tech | IA, tecnologia assistiva, ferramentas digitais, acessibilidade tecnológica e experimentos |
| `2e-resources` | 2e Resources | guias práticos, materiais, bibliotecas, diretórios, checklists e comparativos |

Não criar categorias adicionais sem necessidade editorial demonstrada. Não usar categoria como tag.

## 4. Vocabulário controlado inicial de tags

Tags são assuntos transversais. Usar apenas quando o tema for material ao conteúdo. Tags em minúsculas, sem acentos e em kebab-case; manter os termos legíveis nos títulos e no texto.

### Conceitos e perfis
- `dupla-excepcionalidade` — conceito central 2e.
- `altas-habilidades-superdotacao` — altas habilidades/superdotação.
- `neurodiversidade` — conceito amplo de diversidade neurológica.
- `neurodivergencia` — experiências e perfis neurodivergentes.

### Condições e combinações
- `autismo-tea` — transtorno do espectro autista, quando substantivo ao artigo.
- `tdah` — transtorno do déficit de atenção com hiperatividade.
- `dislexia` — dislexia e dificuldades relacionadas à leitura/escrita, sem usar como sinônimo de todo transtorno de aprendizagem.
- `transtornos-de-aprendizagem` — usar quando o escopo realmente abranger o conjunto de transtornos específicos de aprendizagem.

### Identificação e evidências
- `identificacao` — processos e desafios de identificação.
- `avaliacao` — avaliação educacional, psicológica ou multidimensional, conforme o contexto explicitado.
- `mascaramento` — masking, compensação ou ocultação de forças/dificuldades, quando discutido.
- `pesquisa-cientifica` — síntese, revisão ou discussão explícita de estudos.
- `evidencias` — qualidade, limites e interpretação da evidência.
- `legislacao-politicas-publicas` — leis, normas e políticas públicas.

### Aprendizagem, contexto e participação
- `aprendizagem` — processos e condições de aprender.
- `educacao-inclusiva` — políticas e práticas de inclusão educacional.
- `familia` — experiências, recursos ou orientação geral para famílias.
- `escola` — contexto escolar e práticas institucionais.
- `acessibilidade` — acessibilidade em sentido amplo, especificando o contexto no artigo.
- `desenvolvimento-de-talentos` — oportunidades e desenvolvimento de potencialidades.

### Tecnologia e recursos
- `inteligencia-artificial` — IA como tema substantivo.
- `tecnologia-assistiva` — tecnologia assistiva.
- `ferramentas-digitais` — ferramentas ou serviços digitais analisados.
- `guias-e-materiais` — recursos práticos e materiais produzidos/curados.

A lista é inicial, não uma obrigação de usar todas as tags. Novas tags podem ser propostas quando houver conceito recorrente sem correspondência adequada. Antes de criar uma nova, verificar sinônimos e escolher um termo canônico.

## 5. Regras de atribuição

1. Cada artigo: uma categoria principal, obrigatória.
2. Cada artigo: normalmente 3 a 6 tags relevantes; não existe mínimo artificial.
3. Não adicionar tag só porque a palavra aparece incidentalmente.
4. Não criar tags para nome de autor, periódico, país ou ano.
5. Não usar sinônimos como tags distintas para o mesmo conceito. Preferir o termo canônico.
6. Não confundir condição mencionada como exemplo com foco editorial do artigo.
7. Uma tag não representa diagnóstico, prevalência, endosso ou recomendação.
8. Páginas institucionais e páginas de área não precisam receber tags de artigo.
9. Não transformar automaticamente cada tag em página de SEO. Arquivos de tags só serão criados se houver conteúdo suficiente e utilidade real para navegação.
10. Revisar categoria e tags na pauta, antes da redação final e durante a revisão editorial.

## 6. Metadados obrigatórios dos artigos Jekyll

Exemplo de front matter:

```yaml
---
layout: article
title: "Título claro e fiel ao conteúdo"
description: "Resumo específico, sem promessa exagerada."
categories:
  - 2e-knowledge
tags:
  - dupla-excepcionalidade
  - altas-habilidades-superdotacao
  - identificacao
  - mascaramento
  - pesquisa-cientifica
---
```

Usar a data real de publicação no campo `date`; não retroagir ou antecipar datas para manipular ordenação. O permalink deve ser estável, legível, em minúsculas e com hífens. Não incluir múltiplas categorias para tentar ampliar alcance.

## 7. Governança e manutenção

- Esta página é a fonte única de referência para categorias e tags.
- Mudanças na taxonomia devem ser deliberadas, documentadas e aplicadas aos conteúdos existentes.
- Fazer auditoria quando houver 10 artigos publicados ou antes, se surgirem duplicações.
- Ao renomear uma tag, atualizar todos os artigos e verificar se links/arquivos dependem dela.
- Não criar novas categorias para cada série ou campanha.
- A taxonomia deve melhorar compreensão e navegação humanas; SEO/GEO é consequência, não critério de inflação.
