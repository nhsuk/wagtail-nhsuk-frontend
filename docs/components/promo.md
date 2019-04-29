
# Promo

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import PromoBlock,

class MyPage(Page):
  body = StreamField([
      ...
      ('promo', PromoBlock()),
      ...
  ])
```

# Promo Group
```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import PromoGroupBlock,

class MyPage(Page):
  body = StreamField([
      ...
      ('promo_group', PromoGroupBlock()),
      ...
  ])
```

The promo block will add/remove classes depending on what the user enters in the Wagtail admin interface. 

| Name                | Type     | Required  | Description  |
| --------------------|----------|-----------|--------------|
| **URL**            | string   | Yes       | The value of the promo href attribute |
| **heading**         | string   | Yes       | The text heading of the promo |
| **Image**          | object   | No        | The URL of the image in the promo |
| **Alt text**     | string   | No        | The alternative text for the image|
| **description**     | string   | No        | The text description of the promo |
| **Column**     | string   | Yes        | A choice between one-half and one-third column size |
| **Size**     | string   | Yes        | A choice between either a default or small promo |


## Reference

[Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/promo)
[Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/promo)
