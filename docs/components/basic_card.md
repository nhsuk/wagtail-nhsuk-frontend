
# Basic Card

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import CardBasicBlock,

class MyPage(Page):
  body = StreamField([
      ...
      ('basic_card', CardBasicBlock()),
      ...
  ], use_json_field=True)
```

## Reference

* [Service Manual](https://service-manual.nhs.uk/design-system/components/card#basic-card)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/card#basic-card)
