# Panel

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsstyle.blocks import PanelBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('panel', PanelBlock()),
      ...
  ])
```

## Reference

[Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/panel)
