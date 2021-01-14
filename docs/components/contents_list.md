# Contents List

## Templatetag

```django
{% load nhsukfrontend_tags %}

...

{% contents_list %}
```

The `{% contents_list %}` tag will render a list of sibling pages.

`page.get_url(request)` is used to generate the page url.

`page.title` is used for the labels.

## Template include

```django
{% include 'wagtailnhsukfrontend/contents_list.html' with links=your_links_array %}
```

Including the `wagtailnhsukfrontend/contents_list.html` template will render the contents list.

An array of links should be passed as a template variable

| Option | Description | Default |
| ------ | ----------- | ------- |
| `links` | Array of dicts | [] |
| `links[].label` | Text to display as the link label | |
| `links[].href` | URL to use as the link href | |
| `links[].is_current` | This link is the current page. It will be displayed in a bold font | |

## Reference

* [Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/contents-list)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/contents-list)
