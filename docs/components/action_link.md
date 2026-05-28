# Action Link

```py
from wagtail.models import Page
from wagtail.fields import StreamField

from wagtailnhsukfrontend.blocks import ActionLinkBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('action_link', ActionLinkBlock()),
      ...
  ], use_json_field=True)
```

## Reference

* [Service Manual](https://service-manual.nhs.uk/design-system/components/action-link)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/action-link)
