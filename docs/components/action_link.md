# Action Link

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import ActionLinkBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('action_link', ActionLinkBlock()),
      ...
  ])
```

## Reference

* [Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/action-link)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/action-link)
