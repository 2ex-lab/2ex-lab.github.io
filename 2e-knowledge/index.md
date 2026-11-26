---
layout: page
title: 2e Knowledge
permalink: /2e-knowledge/
description: Ciência, conceitos, pesquisas e questões em aberto sobre dupla excepcionalidade.
category_id: knowledge
---

**Entender conceitos, evidências e limites do conhecimento.**

Esta área reúne conteúdos sobre dupla excepcionalidade (2e), altas habilidades/superdotação, neurodiversidade, identificação, terminologia, pesquisas e debates relevantes.

### Critérios de conteúdo

- Priorizar fontes científicas e institucionais qualificadas.
- Contextualizar população, método e limites dos estudos.
- Não tratar pessoas 2e como um grupo homogêneo.
- Diferenciar associação, causalidade, hipótese e consenso.

## Artigos publicados

{% assign articles = site.categories[page.category_id] %}
{% if articles and articles.size > 0 %}
{% assign articles = articles | sort: "date" | reverse %}
<ul class="post-list">
  {% for post in articles %}
  <li>
    <h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
    <p>{{ post.description | default: post.excerpt | strip_html | normalize_whitespace }}</p>
    <small>{{ post.date | date: "%d/%m/%Y" }}</small>
    {% if post.tags and post.tags.size > 0 %}
    <p class="category-tags">Assuntos:
      {% for tag in post.tags %}
      <a href="{{ '/tags/' | relative_url }}#{{ tag | escape }}">{{ tag | replace: "-", " " }}</a>{% unless forloop.last %}, {% endunless %}
      {% endfor %}
    </p>
    {% endif %}
  </li>
  {% endfor %}
</ul>
{% else %}
<p>Os primeiros artigos desta área estão em preparação.</p>
{% endif %}
