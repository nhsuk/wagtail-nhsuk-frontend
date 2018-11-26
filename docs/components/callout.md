# Action Link

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsstyle.blocks import CalloutBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('callout', CalloutBlock()),
      ...
  ])
```
