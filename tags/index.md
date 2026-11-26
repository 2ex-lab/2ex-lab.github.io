---
layout: page
title: Tags
permalink: /tags/
description: Vocabulário controlado do 2ex-lab e conexões entre os assuntos abordados.
---

As tags conectam conteúdos de diferentes áreas editoriais. Esta é a lista controlada do projeto; uma tag só é atribuída quando o assunto é material para o conteúdo.

Explore também o [índice de categorias]({{ '/categorias/' | relative_url }}) para conhecer as quatro áreas editoriais.

{% assign tag_groups = site.data.taxonomy.tag_groups %}
{% for group in tag_groups %}
## {{ group.name }}

<ul class="taxonomy-list">
  {% for tag in group.tags %}
  {% assign tagged_posts = site.tags[tag.slug] %}
  <li id="{{ tag.slug }}">
    <strong class="tag-name">{{ tag.name | escape }}</strong>
    {% if tagged_posts and tagged_posts.size > 0 %}
    <span class="taxonomy-count"> — {{ tagged_posts.size }} conteúdo(s) publicado(s)</span>
    {% else %}
    <span class="taxonomy-count"> — ainda sem conteúdo publicado</span>
    {% endif %}
    <p>{{ tag.description | escape }}</p>
    {% if tagged_posts and tagged_posts.size > 0 %}
    <ul>
      {% for post in tagged_posts %}
      <li><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></li>
      {% endfor %}
    </ul>
    {% endif %}
  </li>
  {% endfor %}
</ul>
{% endfor %}

<small>Tags sem conteúdo publicado permanecem no vocabulário editorial, mas não geram páginas vazias nem arquivos independentes. A lista será revista quando o acervo crescer.</small>
