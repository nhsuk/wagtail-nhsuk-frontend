# Inset Text

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsstyle.blocks import InsetText

class MyPage(Page):
  body = StreamField([
      ...
      ('inset_text', InsetText()),
      ...
  ])
```
