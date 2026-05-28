# Inset Text

```py
from wagtail.models import Page
from wagtail.fields import StreamField

from wagtailnhsukfrontend.blocks import InsetTextBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('inset_text', InsetTextBlock()),
      ...
  ], use_json_field=True)
```

## Reference

* [Service Manual](https://service-manual.nhs.uk/design-system/components/inset-text)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/inset-text)
