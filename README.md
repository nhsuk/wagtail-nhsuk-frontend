# Wagtail NHS Style

A wagtail implementation of the [NHS frontend](https://github.com/nhsuk/nhsuk-frontend) standard components.

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

from wagtailnhsstyle.blocks import CalloutBlock

class HomePage(Page):
  body = StreamField([
      # Include any of the blocks you want to use.
      ('action_link', ActionLinkBlock()),
      ('callout', CalloutBlock()),
  ])

  content_panels = Page.content_panels + [
      StreamFieldPanel('body'),
  ]
```

Include the CSS in your base template
```html
  <link rel="stylesheet" type="text/css" href="{% static 'wagtailnhsstyle/css/nhsuk.min.css' %}">
```
