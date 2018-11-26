# Action Link

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsstyle.blocks import ActionLinkBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('action_link', ActionLinkBlock()),
      ...
  ])
```
