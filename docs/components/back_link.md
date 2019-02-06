# Back Link

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsstyle.blocks import BackLinkBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('back_link', BackLinkBlock()),
      ...
  ])
```

Add this will give you the ability to add the back link block to the page. If required, this block can also be added through the template.
