# Don't List

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import DontBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('dont_list', DontBlock()),
      ...
  ])
```
## Reference

* [Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/do-and-dont-list)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/do-dont-list)

