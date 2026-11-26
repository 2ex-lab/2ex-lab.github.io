# Taxonomia editorial do 2ex-lab

**Status:** vocabulário controlado implementado em estrutura de dados e navegação.  
**Fonte estruturada:** `_data/taxonomy.yml`.  
**Índice público:** `/tags/`.  
**Princípio:** categorias estáveis e poucas; tags transversais, controladas e aplicadas apenas quando materialmente relevantes.

## 1. Categorias principais

Cada artigo publicado recebe exatamente uma categoria principal. Os identificadores internos do Jekyll são estáveis e distintos dos nomes de navegação.

| Identificador Jekyll | Categoria pública | Escopo |
|---|---|---|
| `knowledge` | **2e Knowledge** | Ciência, conceitos, pesquisas, legislação, identificação e limites do conhecimento |
| `learning` | **2e Learning** | Aprendizagem, educação, família, escola, inclusão e acessibilidade pedagógica |
| `tech` | **2e Tech** | IA, tecnologia assistiva, ferramentas digitais, acessibilidade e experimentação |
| `resources` | **2e Resources** | Guias, materiais, bibliotecas, checklists, diretórios e comparativos |

As URLs públicas das áreas permanecem `/2e-knowledge/`, `/2e-learning/`, `/2e-tech/` e `/2e-resources/`. Não criar sites separados nem categorias adicionais sem necessidade demonstrada.

## 2. Pilares editoriais

Os cinco pilares são dimensões transversais, não categorias nem tags:

- **Entender** — conceitos, evidências, terminologia e identificação.
- **Aprender** — escola, estratégias, acessibilidade pedagógica e apoio.
- **Experimentar** — ferramentas digitais, IA, tecnologia assistiva e métodos.
- **Explorar** — criatividade, interesses, talentos e relatos contextualizados.
- **Escolher** — guias, comparativos e recomendações transparentes.

Podem ser registrados no campo `editorial_pillar`; não geram arquivos de navegação automaticamente.

## 3. Vocabulário controlado de 35 tags

Os slugs e rótulos oficiais ficam em `_data/taxonomy.yml`. O índice público agrupa os termos por assunto e mostra os conteúdos publicados associados.

### Condições, perfis e conceitos
- `dupla-excepcionalidade`
- `altas-habilidades`
- `neurodiversidade`
- `autismo`
- `tdah`
- `dislexia`
- `outras-neurodivergencias`
- `identificacao`
- `desenvolvimento-de-talentos`
- `criatividade`

### Aprendizagem, família e inclusão
- `aprendizagem`
- `educacao-inclusiva`
- `acessibilidade-pedagogica`
- `escola`
- `familia`
- `familia-escola`
- `barreiras-e-apoios`
- `adultos-2e`
- `criancas-e-adolescentes`

### Tecnologia e experimentação
- `inteligencia-artificial`
- `tecnologia-assistiva`
- `acessibilidade-digital`
- `ferramentas-digitais`
- `organizacao-e-planejamento`
- `experimentacao`
- `ux-e-design`

### Evidências, direitos e contexto
- `pesquisa-cientifica`
- `evidencias`
- `legislacao-e-direitos`
- `brasil`
- `relatos-contextualizados`

### Recursos e decisões
- `guias-praticos`
- `checklists-e-modelos`
- `comparativos`
- `bibliotecas-e-diretorios`
- `recomendacoes-transparentes`

## 4. Regras de atribuição

1. Uma categoria principal por artigo; categoria secundária somente se houver interseção editorial genuína.
2. Normalmente, 2 a 6 tags específicas por conteúdo; não existe mínimo artificial.
3. Não atribuir tag por mera menção incidental.
4. Não criar tags para cada artigo, sinônimos, marcas comerciais, anos ou palavras genéricas.
5. Criar tag nova somente quando houver recorrência editorial e ganho real de descoberta.
6. Público, formato, estado da evidência, sensibilidade, situação comercial, fontes e data de revisão são metadados próprios, não tags.
7. Páginas de categoria listam automaticamente os artigos publicados na categoria.
8. Os chips de tags nos artigos levam ao ponto correspondente no índice transversal `/tags/#slug`.
9. O índice mostra tags ainda sem conteúdo, mas não cria arquivos de tag vazios nem páginas SEO independentes.
10. Ligações editoriais devem ser contextuais; não forçar conexões só porque dois artigos compartilham uma tag ampla.

## 5. Conexões editoriais

- Dupla excepcionalidade conecta-se a altas habilidades, neurodiversidade, identificação e evidências.
- Identificação pode conectar-se a família, escola, barreiras e apoios, respeitando o foco de cada conteúdo.
- Aprendizagem conecta-se a acessibilidade pedagógica, educação inclusiva e recursos práticos.
- Tecnologia deve explicar qual problema de acesso ou aprendizagem aborda, além de suas limitações.
- Recursos práticos devem apontar para os conceitos, critérios ou evidências que fundamentam seu uso ou recomendação.

As tags ajudam a descobrir essas relações, mas não representam causalidade, diagnóstico, prevalência ou endosso.

## 6. Metadados editoriais

Quando pertinentes, usar campos como `editorial_pillar`, `content_type`, `audience`, `evidence_status`, `sensitivity`, `commercial_status`, `reviewed_at`, `sources` e `related_content`. Não criar páginas públicas para esses campos sem decisão específica.

## 7. Governança

Revisar a taxonomia após os primeiros 10–15 conteúdos publicados ou antes se surgirem duplicações. Ao renomear um slug, atualizar todos os conteúdos e verificar links. A taxonomia deve melhorar a navegação humana; SEO/GEO é consequência, não justificativa para inflar tags.
