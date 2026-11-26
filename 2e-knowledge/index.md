---
layout: page
title: 2e Knowledge
permalink: /2e-knowledge/
description: Ciência, conceitos, pesquisas e questões em aberto sobre dupla excepcionalidade.
---

**Entender conceitos, evidências e limites do conhecimento.**

Esta área reunirá conteúdos sobre dupla excepcionalidade (2e), altas habilidades/superdotação, neurodivergência, identificação, terminologia, pesquisas e debates relevantes.

### Critérios de conteúdo

- Priorizar fontes científicas e institucionais qualificadas.
- Contextualizar população, método e limites dos estudos.
- Não tratar pessoas 2e como um grupo homogêneo.
- Diferenciar associação, causalidade, hipótese e consenso.

## Artigos publicados

{% assign articles = site.categories["2e-knowledge"] | sort: "date" | reverse %}
{% if articles and articles.size > 0 %}
<ul class="post-list">
  {% for post in articles %}
  <li>
    <h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
    <p>{{ post.description | default: post.excerpt | strip_html | normalize_whitespace }}</p>
    <small>{{ post.date | date: "%d/%m/%Y" }}</small>
  </li>
  {% endfor %}
</ul>
{% else %}
<p>Os primeiros artigos desta área estão em preparação.</p>
{% endif %}
