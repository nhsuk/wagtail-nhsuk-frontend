# Care Card

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsstyle.blocks import CareCardBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('care_card', CareCardBlock()),
      ...
  ])
```
