# Wagtail NHS Style

A wagtail implementation of the [NHS frontend v0.8.0](https://github.com/nhsuk/nhsuk-frontend) standard components.

# Installation

Install the pypi package
```
pip install wagtail-nhs-style
```

Add to your `INSTALLED_APPS` in wagtail settings
```python
INSTALLED_APPS = [
  ...

  'wagtailnhsstyle',

  ...
]
```

Use blocks in your streamfields
```python
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsstyle.blocks import ActionLinkBlock, WarningCalloutBlock

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
{% load nhsstyle_tags %}

<html>
...
<body>
  {% breadcrumbs %}
</body>
</html>
```

Use template includes
```django
{% include 'wagtailnhsstyle/header.html' with show_search=True %}
```

See the [component documentation](./docs/components/) for a list of components you can use.

Include the CSS in your base template
```html
  <link rel="stylesheet" type="text/css" href="{% static 'wagtailnhsstyle/css/wagtail-nhs.min.css' %}">
```

Include the Javascript in your base template
```html
  <script type="text/javascript" src="{% static 'wagtailnhsstyle/js/nhsuk-0.8.0.min.js' %}" defer></script>
```

# Further reading

See more [documentation](./docs/)
