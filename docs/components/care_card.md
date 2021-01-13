# Care Card

```py
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import CareCardBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('care_card', CareCardBlock()),
      ...
  ])
```

By default, the care card block can contain the following sub-blocks:

* [RichTextBlock](https://docs.wagtail.io/en/v2.7/topics/streamfield.html#richtextblock)
* [ActionLinkBlock](./action_link.md)
* [DetailsBlock](./details.md)
* [InsetTextBlock](./inset_text.md)
* [ImageBlock](./image.md)
* [WarningCalloutBlock](./warning_callout.md)
* [SummaryListBlock](./summary_list.md)

To add extra sub-blocks, you must extend the `CareCardBlock` class.
```py
class CustomCareCardBody(CareCardBlock.BodyStreamBlock):

  # Add a custom block
  extra = MyExtraBlock()


class CustomCareCardBlock(CareCardBlock):

  body = CustomCareCardBody(required=True)


class MyPage(Page):
  body = StreamField([
      ...
      ('care_card', CustomCareCardBlock()),
      ...
  ])
```

## Reference

* [Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/care-cards)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/care-card)
