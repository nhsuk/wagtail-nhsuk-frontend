# Breadcrumb

```django
{% load nhsukfrontend_tags %}

<html>
...
<body>
  {% breadcrumbs %}
</body>
</html>
```

The `{% breadcrumbs %}` tag will render a breadcrumb with a link to every parent
page up to and including your site root.

For example if you have a page at `/page1/page2/page3/`, the breadcrumb will
show `Home > Page1 > Page2`.

URLs are generated with the wagtail [pageurl](http://docs.wagtail.io/en/v2.0/topics/writing_templates.html#pageurl)
tag.

`page.title` is used for the page names.
