
# Card 

Contains the different viarants of a card

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import CardBlock,

class MyPage(Page):
  body = StreamField([
      ...
      ('card', CardBlock()),
      ...
  ])
```

# Card Group

A Card Group is a collection of cards in a 2-column or 3-column grid layout.

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import CardGroupBlock,

class MyPage(Page):
  body = StreamField([
      ...
      ('card_group', CardGroupBlock()),
      ...
  ])
```





## Reference

[Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/card)