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
  ])
```

## Reference

* [Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/warning-callout)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/warning-callout)
