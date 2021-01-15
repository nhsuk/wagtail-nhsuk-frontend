# Feature Card

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import CardFeatureBlock,

class MyPage(Page):
  body = StreamField([
      ...
      ('clickable_card', CardFeatureBlock()),
      ...
  ])
```

## Reference

* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/card#feature)
