# Do List

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import DoBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('do_list', DoBlock()),
      ...
  ])
```

## Reference

* [Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/do-and-dont-list)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/do-dont-list)

