# Review Date

Use this code snippet to include the review date component. This snipped has to be pasted in `home/models.py` and then added to the page through the Wagtail admin interface.



To include the review date component on the page you will have to add this snippet of code in the template:
```django
  {% include "wagtailnhsukfrontend/review_date.html" %}
```
Add the snippet below to the imports in the `models.py` file:
```py
from wagtailnhsukfrontend.mixins import (
    ReviewDateMixin,
)
```
 Modify your page class to add the `ReviewDataMixin` like so:
```py
class  MyPage(Page, ReviewDateMixin):

    settings_panels = Page.settings_panels + ReviewDateMixin.settings_panels
```

You can modify the component settings in the page settings tab on the Wagtail admin interface.


# Reference

[Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/review-date)  
[Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/review-date)
