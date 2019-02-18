# Panel

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsstyle.blocks import PanelBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('panels', PanelBlock()),
      ...
  ])
```
