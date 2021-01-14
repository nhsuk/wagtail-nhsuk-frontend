# Pagination

## Templatetag

```django
{% load nhsukfrontend_tags %}

...

{% pagination %}
```

The `{% pagination %}` tag will render next and previous page links to sibling pages.

`page.get_url(request)` is used to generate the page url.

`page.title` is used for the labels.


## Template include

```django
{% include 'wagtailnhsukfrontend/pagination.html' with prev_url="./previous/" next_url="./next/" %}
```

Including the `wagtailnhsukfrontend/pagination.html` template will render next and previous links.

There are some options that can be passed to the pagination:

| Option | Description | Default |
| ------ | ----------- | ------- |
| `prev_url` | URL for when the Previous button is clicked | `None` |
| `prev_label` | Label underneath the Previous button | `None` |
| `next_url` | URL for when the Next button is clicked | `None` |
| `next_label` | Label underneath the Next button | `None` |

If `prev_url` and `next_url` are unspecified, the relevant link will not be shown.

## Reference

* [Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/pagination)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/pagination)

