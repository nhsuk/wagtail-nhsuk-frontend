# Dont List

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsstyle.blocks import DontBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('dont_list', DontBlock()),
      ...
  ])
```
