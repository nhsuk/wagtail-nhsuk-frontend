# Inset Text

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import InsetTextBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('inset_text', InsetTextBlock()),
      ...
  ])
```

## Reference

* [Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/inset-text)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/inset-text)
