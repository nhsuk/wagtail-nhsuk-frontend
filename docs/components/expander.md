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

By default, the expander block can contain the following sub-blocks:

* [RichTextBlock](https://docs.wagtail.io/en/v2.7/topics/streamfield.html#richtextblock)
* [ActionLinkBlock](./action_link.md)
* [InsetTextBlock](./inset_text.md)
* [ImageBlock](./image.md)
* [GreyPanelBlock](./grey_panel.md)
* [WarningCalloutBlock](./warning_callout.md)
* [SummaryListBlock](./summary_list.md)

To add extra sub-blocks, you must extend the `ExpanderBlock` class.
```py
class CustomExpanderBody(ExpanderBlock.BodyStreamBlock):

  # Add a custom block
  extra = MyExtraBlock()


class CustomExpanderBlock(ExpanderBlock):

  body = CustomExpanderBody(required=True)


class MyPage(Page):
  body = StreamField([
      ...
      ('expander', CustomExpanderBlock()),
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

* [Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/expander)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/details)
