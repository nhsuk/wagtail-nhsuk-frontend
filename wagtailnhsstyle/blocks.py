from wagtail.core.blocks import (
    CharBlock,
    RichTextBlock,
    StructBlock,
    URLBlock,
)


class ActionLinkBlock(StructBlock):

    text = CharBlock(label="link text", required=True)
    external_url = URLBlock(label="external URL", required=True)

    class Meta:
        template = 'wagtailnhsstyle/action_link.html'


class CalloutBlock(RichTextBlock):

    class Meta:
        template = 'wagtailnhsstyle/callout.html'
