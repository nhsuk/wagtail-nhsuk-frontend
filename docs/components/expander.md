# Expander

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import ExpanderBlock,

class MyPage(Page):
  body = StreamField([
      ...
      ('expander', ExpanderBlock()),
      ...
  ])
```

# Expander Group

An expander group should be used when multiple expanders are required in a list.

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import ExpanderGroupBlock,

class MyPage(Page):
  body = StreamField([
      ...
      ('group_expander', ExpanderGroupBlock()),
      ...
  ])
```

## Reference

[Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/expander)
[Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/details)
