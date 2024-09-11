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
  ], use_json_field=True)
```

By default, the details block can contain the following sub-blocks:

* [RichTextBlock](https://docs.wagtail.io/en/v2.7/topics/streamfield.html#richtextblock)
* [ActionLinkBlock](./action_link.md)
* [InsetTextBlock](./inset_text.md)
* [ImageBlock](./image.md)
* [WarningCalloutBlock](./warning_callout.md)
* [SummaryListBlock](./summary_list.md)

To add extra sub-blocks, you must extend the `DetailsBlock` class.
```py
class CustomDetailsBody(DetailsBlock.BodyStreamBlock):

  # Add a custom block
  extra = MyExtraBlock()


class CustomDetailsBlock(DetailsBlock):

  body = CustomDetailsBody(required=True)


class MyPage(Page):
  body = StreamField([
      ...
      ('details', CustomDetailsBlock()),
      ...
  ], use_json_field=True)
```

## Reference

* [Service Manual](https://service-manual.nhs.uk/design-system/components/details)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/details)
