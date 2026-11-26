---
layout: page
title: 2e Learning
permalink: /2e-learning/
description: Aprendizagem, família, escola e inclusão.
category_id: learning
---

**Explorar condições para aprender e participar.**

Esta área reúne conteúdos sobre aprendizagem, família, escola, educação inclusiva, acessibilidade pedagógica, potencialidades, barreiras e necessidades de apoio.

A abordagem respeita diferentes contextos e evita receitas universais. Experiências individuais são identificadas como experiências, não como evidência geral.

## Artigos publicados

{% assign articles = site.categories[page.category_id] | sort: "date" | reverse %}
{% if articles and articles.size > 0 %}
<ul class="post-list">
  {% for post in articles %}
  <li><h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3><p>{{ post.description | default: post.excerpt | strip_html | normalize_whitespace }}</p></li>
  {% endfor %}
</ul>
{% else %}
<p>Os primeiros artigos desta área estão em preparação.</p>
{% endif %}
