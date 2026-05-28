# Summary List

```py
from wagtail.models import Page
from wagtail.fields import StreamField

from wagtailnhsukfrontend.blocks import SummaryListBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('summary_list', SummaryListBlock()),
      ...
  ], use_json_field=True)
```

## Reference

* [Service Manual](https://service-manual.nhs.uk/design-system/components/summary-list)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/summary-list)

