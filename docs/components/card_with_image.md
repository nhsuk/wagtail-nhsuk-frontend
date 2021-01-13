
# Card with an image

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import CardImageBlock,

class MyPage(Page):
  body = StreamField([
      ...
      ('card_with_an_image', CardImageBlock()),
      ...
  ])
```

## Reference

* [Service Manual](https://service-manual.nhs.uk/design-system/components/card#card-with-an-image)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/card#card-with-an-image)
