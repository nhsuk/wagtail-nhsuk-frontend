# header

```django
{% include 'wagtailnhsstyle/header.html' %}
```

Including the `wagtailnhsstyle/header.html` template will render the NHS header.

There are some options that can be passed to the header:

| Option | description | default |
| ------ | ----------- | ------- |
| service_name | Title to display on the header | `None` |
| service_long_name | Set to `True` to give more room for the service name | `False` |
| service_href | URL for when the service name is clicked | `"/"` |
| logo_href | URL for when the NHS logo is clicked | `"/"` |
| logo_aria | Aria label for the NHS logo | `"NHS Homepage"` |
| transactional | Set to `True` to display a smaller header, suitable for a transactional service | `False` |
| show_search | Set to `True` to show the search bar | `False` |
| primary_links | An array of dicts containing navigation items | `None` |
| primary_links[]['label'] | Navigation item label | `None` |
| primary_links[]['url'] | Navigation item url | `None` |

## Examples

### Header with a search box

```django
{% include 'wagtailnhsstyle/header.html' with show_search=True %}
```

### Header with navigation

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
{% include 'wagtailnhsstyle/header.html' with primary_links=navigation %}
```

### Header for a transactional service

```django
{% include 'wagtailnhsstyle/header.html' with transactional="True" service_name="Find a Pharmacy" service_href="/find-a-pharmacy" %}
```
