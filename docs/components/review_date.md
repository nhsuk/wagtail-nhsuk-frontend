# Review Date

Add the `ReviewDateMixin` to your page model:
```py
from wagtailnhsukfrontend.mixins import (
    ReviewDateMixin,
)

class MyPage(Page, ReviewDateMixin):

    ...

    settings_panels = Page.settings_panels + ReviewDateMixin.settings_panels
```

The `ReviewDateMixin` will add `last_review_date` and `next_review_date` fields to your page model,
editable in the settings panel of the wagtail page edit interface.

To include the review date component on a page you will have to include the review date template in your page template:
```django
  {% include "wagtailnhsukfrontend/review_date.html" %}
```

# Reference

* [Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/review-date)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/review-date)
