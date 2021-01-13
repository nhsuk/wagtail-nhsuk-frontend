# Header

## Wagtail Site Settings

wagtail-nhs-style comes with a wagtail
[site settings](http://docs.wagtail.io/en/v2.4/reference/contrib/settings.html)
model. If you want to allow CMS users to configure the header in the wagtail
interface, use of the site setting is recommended.

Add the `wagtailnhsukfrontend.settings` module to your `INSTALLED_APPS` config.

```python
INSTALLED_APPS = [
  ...
  'wagtailnhsukfrontend',
  'wagtailnhsukfrontend.settings',
  ...
]
```

This will create a new option under `Settings > Header settings` in the
wagtail interface.

To include the header in your template, use the `header` templatetag.

```python
{% load nhsukfrontendsettings_tags %}

...

<body>
  {% header %}
  ...
</body>
```

If search is going to be used, the search endpoint will probably need to be configured.

```
  {% header search_action="/s/" search_field_name="q" %}
```

## Direct use of templates

```django
{% include 'wagtailnhsukfrontend/header.html' %}
```

Including the `wagtailnhsukfrontend/header.html` template will render the NHS header.

There are some options that can be passed to the header:

| Option | Description | Default |
| ------ | ----------- | ------- |
| `service_name` | Title to display on the header | `None` |
| `service_long_name` | Set to `True` to give more room for the service name | `False` |
| `service_href` | URL for when the service name is clicked | `"/"` |
| `logo_href` | URL for when the NHS logo is clicked | `"/"` |
| `logo_aria` | Aria label for the NHS logo | `"NHS Homepage"` |
| `transactional` | Set to `True` to display a smaller header, suitable for a transactional service | `False` |
| `show_search` | Set to `True` to show the search bar | `False` |
| `search_action` | Value to use as the search <form> `action` attribute | `/search/` |
| `search_field_name` | Value to use as the search <input> `name` attribute | `search-input` |
| `primary_links` | An array of dicts containing navigation items | `None` |
| `primary_links[].label` | Navigation item label | `None` |
| `primary_links[].url` | Navigation item url | `None` |

### Examples

#### Header with a search box

```django
{% include 'wagtailnhsukfrontend/header.html' with show_search=True %}
```

#### Header with custom search endpoint

```django
{% include 'wagtailnhsukfrontend/header.html' with show_search=True search_action="/s/" search_field_name="q"  %}
```

Performing a search with these settings will result in the user navigating to `/s/?q=search-term` instead of the
default `/search/?search-input=search-term`

#### Header with navigation

Assuming `navigation` is added to the context somehow, for example with a
[context_processor](https://docs.djangoproject.com/en/1.11/ref/templates/api/#writing-your-own-context-processors)
or with a [wagtial site setting](http://docs.wagtail.io/en/v2.1.1/reference/contrib/settings.html).

```python
# Your custom context_processor
def navigation(request):
  return {
    'navigation': [
      { "label": "One", "url": "/one" },
      { "label": "Two", "url": "/two" },
      { "label": "Three", "url": "/three" },
      { "label": "Four", "url": "/four" },
    ]
  }

```

```django
{% include 'wagtailnhsukfrontend/header.html' with primary_links=navigation %}
```

#### Header for a transactional service

```django
{% include 'wagtailnhsukfrontend/header.html' with transactional="True" service_name="Find a Pharmacy" service_href="/find-a-pharmacy" %}
```

## Reference

* [Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/header)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/header)
