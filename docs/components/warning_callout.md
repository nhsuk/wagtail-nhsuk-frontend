# Warning Callout

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import WarningCalloutBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('warning_callout', WarningCalloutBlock()),
      ...
  ])
```
