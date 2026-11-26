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

{% assign articles = site.categories[page.category_id] %}
## Artigos publicados

{% if articles and articles.size > 0 %}
<p class="taxonomy-count">{{ articles.size }} conteúdo(s) publicado(s) nesta área. <a href="{{ '/categorias/' | relative_url }}">Ver todas as categorias</a> ou <a href="{{ '/tags/' | relative_url }}">explorar tags</a>.</p>
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
      <a class="tag-link" href="{{ '/tags/' | relative_url }}#{{ tag | escape }}">{{ tag | replace: "-", " " }}</a>{% unless forloop.last %}, {% endunless %}
      {% endfor %}
    </p>
    {% endif %}
  </li>
  {% endfor %}
</ul>
{% else %}
<p>Ainda não há artigos publicados nesta área. Consulte o <a href="{{ '/categorias/' | relative_url }}">índice de categorias</a> ou o <a href="{{ '/tags/' | relative_url }}">índice de tags</a>.</p>
{% endif %}
