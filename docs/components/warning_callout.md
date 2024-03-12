# Warning Callout

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import WarningCalloutBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('warning_callout', WarningCalloutBlock()),
      ...
  ], use_json_field=True)
```

## Reference

* [Service Manual](https://service-manual.nhs.uk/design-system/components/warning-callout)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/warning-callout)
