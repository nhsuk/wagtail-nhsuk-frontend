# Details

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import DetailsBlock,

class MyPage(Page):
  body = StreamField([
      ...
      ('details', DetailsBlock()),
      ...
  ])
```

## Reference

[Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/details)
[Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/details)
