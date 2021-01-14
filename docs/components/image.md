# Images

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import ImageBlock


class HomePage(Page):

    parent_page_types = ['wagtailcore.Page']

    body = StreamField([
        ...
        ('captionable_image', ImageBlock()),
        ...
```
## Reference

* [Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/images)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/images)
