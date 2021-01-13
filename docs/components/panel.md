# Panel - DEPRECATED

Replaced with the [Card](./card.md) component

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import PanelBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('panel', PanelBlock()),
      ...
  ])
```

## Reference

[Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/card)
