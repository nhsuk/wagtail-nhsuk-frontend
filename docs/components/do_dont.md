# Inset Text

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsstyle.blocks import DoDontBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('do_and_dont_list', DoDontBlock()),
      ...
  ])
```
