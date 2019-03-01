# Inset Text

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsstyle.blocks import DoBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('do_list', DoBlock()),
      ...
  ])
```
