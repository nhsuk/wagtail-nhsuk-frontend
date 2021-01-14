# Breadcrumb

```django
{% load nhsukfrontend_tags %}

<html>
...
<body>
  {% breadcrumb %}
</body>
</html>
```

The `{% breadcrumb %}` tag will render a breadcrumb with a link to every parent
page up to and including your site root.

For example if you have a page at `/page1/page2/page3/`, the breadcrumb will
show `Home > Page1 > Page2`.

URLs are generated with the wagtail [pageurl](http://docs.wagtail.io/en/v2.0/topics/writing_templates.html#pageurl)
tag.

`page.title` is used for the page names.

## Reference

* [Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/back-link)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/back-link)
