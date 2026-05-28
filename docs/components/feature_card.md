# Feature Card

```py
from wagtail.models import Page
from wagtail.fields import StreamField

from wagtailnhsukfrontend.blocks import CardFeatureBlock,

class MyPage(Page):
  body = StreamField([
      ...
      ('clickable_card', CardFeatureBlock()),
      ...
  ], use_json_field=True)
```

## Reference

* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/card#feature)
