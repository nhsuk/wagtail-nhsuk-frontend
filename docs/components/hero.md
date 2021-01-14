# Hero

Add the `HeroMixin` to your page model:
```py
from wagtailnhsukfrontend.mixins import (
    HeroMixin,
)

class MyPage(HeroMixin, Page):

    ...

    content_panels = Page.content_panels + HeroMixin.content_panels + ...
```

The `HeroMixin` will add fields to your page model, allowing the Hero component to be edited in the
contents panels of the wagtail cms.

To include the Hero component on a page you will have to include the Hero template in your page template:
```django
  {% include "wagtailnhsukfrontend/hero.html" %}
```

The Hero component should be displayed at full width, rather than at two-thirds like many other 
components.


## Reference

* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/hero)
