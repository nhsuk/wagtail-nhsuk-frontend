# Inset Text

```py
from wagtail.models import Page
from wagtail.fields import StreamField

from wagtailnhsukfrontend.blocks import TagBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('tag', TagBlock()),
      ...
  ], use_json_field=True)
```

## Reference

* [Service Manual](https://service-manual.nhs.uk/design-system/components/tag)
