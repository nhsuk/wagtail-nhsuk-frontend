# Care Card

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import CareCardBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('care_card', CareCardBlock()),
      ...
  ])
```

## Reference

[Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/care-cards)
[Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/care-card)
