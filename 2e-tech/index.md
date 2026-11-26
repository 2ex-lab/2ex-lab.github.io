---
layout: page
title: 2e Tech
permalink: /2e-tech/
description: Tecnologia, inteligência artificial, tecnologia assistiva e acessibilidade.
category_id: tech
---

**Experimentar tecnologia com propósito e senso crítico.**

Esta área reúne explorações de ferramentas digitais, inteligência artificial, tecnologia assistiva, acessibilidade, organização e apoio à aprendizagem.

Quando houver testes práticos, serão documentados contexto, critérios, compatibilidade, custos, privacidade, limitações e data da avaliação. Não afirmaremos que uma ferramenta foi testada sem que isso tenha ocorrido.

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
      <a href="{{ '/tags/' | relative_url }}#{{ tag | escape }}">{{ tag | replace: "-", " " }}</a>{% unless forloop.last %}, {% endunless %}
      {% endfor %}
    </p>
    {% endif %}
  </li>
  {% endfor %}
</ul>
{% else %}
<p>Ainda não há artigos publicados nesta área. Consulte o <a href="{{ '/categorias/' | relative_url }}">índice de categorias</a> ou o <a href="{{ '/tags/' | relative_url }}">índice de tags</a>.</p>
{% endif %}
