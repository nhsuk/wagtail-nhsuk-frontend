# Care Card (deprecated)

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

# Default Heading Level

The default heading level for care cards is 3 but this can be overwritten using a Django setting.
See testapp/testapp/settings/base.py as an example.
If no setting is supplied the default will remain 3.

## Reference

* [Service Manual](https://service-manual.nhs.uk/design-system/patterns/help-users-decide-when-and-where-to-get-care)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/card)
