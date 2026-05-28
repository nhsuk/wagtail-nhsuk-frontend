
# Clickable Card

```py
from wagtail.models import Page
from wagtail.fields import StreamField

from wagtailnhsukfrontend.blocks import CardClickableBlock,

class MyPage(Page):
  body = StreamField([
      ...
      ('clickable_card', CardClickableBlock()),
      ...
  ], use_json_field=True)
```

## Reference

* [Service Manual](https://service-manual.nhs.uk/design-system/components/card#clickable-card)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/card#clickable-card)
