# Wagtail NHS.UK frontend

A wagtail implementation of the [NHS frontend v4.0.0](https://github.com/nhsuk/nhsuk-frontend) standard components.

## Installation

Install the pypi package
```
pip install wagtail-nhsuk-frontend
```

Add to your `INSTALLED_APPS` in wagtail settings
```python
INSTALLED_APPS = [
  ...

  'wagtailnhsukfrontend',

  ...
]
```

Use blocks in your streamfields
```python
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import ActionLinkBlock, WarningCalloutBlock

class HomePage(Page):
  body = StreamField([
      # Include any of the blocks you want to use.
      ('action_link', ActionLinkBlock()),
      ('callout', WarningCalloutBlock()),
  ])

  content_panels = Page.content_panels + [
      StreamFieldPanel('body'),
  ]
```

Use templatetags
```django
{% load nhsukfrontend_tags %}

<html>
...
<body>
  {% breadcrumb %}
</body>
</html>
```

Use template includes
```django
{% include 'wagtailnhsukfrontend/header.html' with show_search=True %}
```

See the [component documentation](./docs/components/) for a list of components you can use.

Include the CSS in your base template
```html
  <link rel="stylesheet" type="text/css" href="{% static 'wagtailnhsukfrontend/css/wagtail-nhsuk-frontend.min.css' %}">
```

Include the Javascript in your base template
```html
  <script type="text/javascript" src="{% static 'wagtailnhsukfrontend/js/nhsuk-4.0.0.min.js' %}" defer></script>
```

Define a custom search API and endpoint
```js
    <script>
      window.NHSUK_SETTINGS = {};
      window.NHSUK_SETTINGS.SUGGESTIONS_TEST_HOST = "[CUSTOM API]";
      window.NHSUK_SETTINGS.SEARCH_TEST_HOST = "[CUSTOM ENDPOINT]";
    </script> 
```

## Contributing

See the [contributing documentation](./docs/contributing.md) to run the application locally and contribute changes.

## Further reading

See more [documentation](./docs/)
