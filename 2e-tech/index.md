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

## Artigos publicados

{% assign articles = site.categories[page.category_id] %}
{% if articles and articles.size > 0 %}
{% assign articles = articles | sort: "date" | reverse %}
<ul class="post-list">
  {% for post in articles %}
  <li><h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3><p>{{ post.description | default: post.excerpt | strip_html | normalize_whitespace }}</p></li>
  {% endfor %}
</ul>
{% else %}
<p>Nenhum artigo foi publicado nesta área até o momento.</p>
{% endif %}
