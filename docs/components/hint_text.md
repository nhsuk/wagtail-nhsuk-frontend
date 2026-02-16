# Inset Text

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import HintTextBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('hint_text', HintTextBlock()),
      ...
  ], use_json_field=True)
```

## Reference

* [Service Manual](https://service-manual.nhs.uk/design-system/components/hint-text)
