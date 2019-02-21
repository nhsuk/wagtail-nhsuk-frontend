# Review Date

Use this code snippet to include the review date component. This snipped has to be pasted in `home/models.py' and then added to the page through the Wagtail admin interface.

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import ReviewDateBlock,

class MyPage(Page):
  body = StreamField([
      ...
      ('review_date', ReviewDateBlock()),
      ...
  ])
```
