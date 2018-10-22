from wagtail.core.blocks import RichTextBlock

class CalloutBlock(RichTextBlock):

    class Meta:
        template = 'wagtailnhsstyle/callout.html'
