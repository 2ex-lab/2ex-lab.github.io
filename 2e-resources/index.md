---
layout: page
title: 2e Resources
permalink: /2e-resources/
description: Guias, materiais, bibliotecas e recursos selecionados.
category_id: resources
---

**Encontrar recursos com contexto e critérios claros.**

Esta área reúne guias, materiais, bibliotecas, referências e comparativos úteis para pessoas 2e, famílias, educadores e profissionais.

## Acessibilidade para toda a comunidade

A curadoria poderá incluir recursos para:

- acesso à informação, leitura e compreensão;
- comunicação e comunicação alternativa;
- navegação digital e interação;
- organização, planejamento e aprendizagem;
- legendas, transcrições e diferentes formatos de conteúdo;
- uso em dispositivos variados e condições de baixa conectividade.

A seleção considerará finalidade, público e contexto, custo, idioma, privacidade, compatibilidade, limitações e qualidade das evidências disponíveis. Serão consideradas deficiências visuais, auditivas, motoras e intelectuais, diferenças de linguagem e comunicação, neurodivergências, necessidades temporárias e barreiras contextuais.

Não apresentaremos ferramentas como testadas ou recomendadas sem avaliação documentada.

{% assign articles = site.categories[page.category_id] %}
## Recursos publicados

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
<p>Ainda não há recursos publicados nesta área. Consulte o <a href="{{ '/categorias/' | relative_url }}">índice de categorias</a> ou o <a href="{{ '/tags/' | relative_url }}">índice de tags</a>.</p>
{% endif %}
