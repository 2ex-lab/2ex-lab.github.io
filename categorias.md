---
layout: page
title: Categorias
permalink: /categorias/
description: Áreas editoriais do 2ex-lab e conteúdos publicados em cada uma.
---

As quatro categorias organizam a publicação por área editorial. São estáveis e complementares: cada artigo pertence a uma categoria principal, enquanto as tags conectam assuntos que atravessam diferentes áreas.

{% assign categories = site.data.taxonomy.categories %}
<ul class="taxonomy-list category-index">
  {% for category in categories %}
  {% assign category_posts = site.categories[category.slug] %}
  <li id="{{ category.slug }}">
    <h2><a href="{{ category.url | relative_url }}">{{ category.title | escape }}</a></h2>
    <p>{{ category.description | escape }}</p>
    {% if category_posts and category_posts.size > 0 %}
    <p class="taxonomy-count">{{ category_posts.size }} conteúdo(s) publicado(s)</p>
    {% assign category_posts = category_posts | sort: "date" | reverse %}
    <ul>
      {% for post in category_posts %}
      <li><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></li>
      {% endfor %}
    </ul>
    {% else %}
    <p class="taxonomy-count">Ainda sem conteúdos publicados</p>
    {% endif %}
  </li>
  {% endfor %}
</ul>

## Explore por assunto

Uma mesma questão pode aparecer em mais de uma área editorial. Use o [índice de tags]({{ '/tags/' | relative_url }}) para encontrar conteúdos relacionados por tema, conceito ou recurso.
