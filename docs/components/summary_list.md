# Summary List

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import SummaryListBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('summary_list', SummaryListBlock()),
      ...
  ])
```

## Reference

* [Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/summary-list)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/summary-list)

