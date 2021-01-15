
# Clickable Card

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import CardClickableBlock,

class MyPage(Page):
  body = StreamField([
      ...
      ('clickable_card', CardClickableBlock()),
      ...
  ])
```

## Reference

* [Service Manual](https://service-manual.nhs.uk/design-system/components/card#clickable-card)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/card#clickable-card)
