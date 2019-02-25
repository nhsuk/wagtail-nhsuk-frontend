
# Details, expanders and expander group

Use this code snippet to include the details, expander and expander group component. This snipped has to be pasted in `home/models.py' and then add to the page through the Wagtail admin interface.

# Details

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import DetailsBlock,

class MyPage(Page):
  body = StreamField([
      ...
      ('details', DetailsBlock()),
      ...
  ])
```

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

# Group Expander

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

# Reference

[Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/details)
[Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/details)
