from wagtail.core.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StructBlock,
    URLBlock,
    ListBlock,
)
from wagtail.images.blocks import ImageChooserBlock


class ActionLinkBlock(StructBlock):

    text = CharBlock(label="link text", required=True)
    external_url = URLBlock(label="external URL", required=True)

    class Meta:
        template = 'wagtailnhsukfrontend/action_link.html'


class CareCardBlock(StructBlock):

    type = ChoiceBlock([
        ('primary', 'Primary'),
        ('urgent', 'Urgent'),
        ('immediate', 'Immediate'),
    ], required=True)
    title = CharBlock(required=True)
    body = RichTextBlock(required=True)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context['accessible_title_prefix'] = {
            'primary': 'Non-urgent advice: ',
            'urgent': 'Urgent advice:',
            'immediate': 'Immediate action required:',
        }[value['type']]
        return context

    class Meta:
        template = 'wagtailnhsukfrontend/care_card.html'


class WarningCalloutBlock(RichTextBlock):

    class Meta:
        template = 'wagtailnhsukfrontend/warning_callout.html'


class InsetTextBlock(RichTextBlock):

    class Meta:
        template = 'wagtailnhsukfrontend/inset_text.html'


class DetailsBlock(StructBlock):

    title = CharBlock(required=True)
    body = RichTextBlock(required=True)

    class Meta:
        template = 'wagtailnhsukfrontend/details.html'


class ExpanderBlock(DetailsBlock):

    class Meta:
        template = 'wagtailnhsukfrontend/expander.html'


class ExpanderGroupBlock(StructBlock):

    expanders = ListBlock(ExpanderBlock)

    class Meta:
        template = 'wagtailnhsukfrontend/expander_group.html'


class PanelBlock(StructBlock):

    labeled_title = CharBlock(required=False)
    body = RichTextBlock(required=True)

    class Meta:
        template = 'wagtailnhsukfrontend/panel.html'


class DoBlock(StructBlock):

    do = ListBlock(RichTextBlock)

    class Meta:
        template = 'wagtailnhsukfrontend/do_list.html'


class DontBlock(StructBlock):

    dont = ListBlock(RichTextBlock)

    class Meta:
        template = 'wagtailnhsukfrontend/dont_list.html'


class ImageBlock(StructBlock):

    content_image = ImageChooserBlock(required=True)
    alt_text = CharBlock(required=False, help_text="Only leave this blank if the image is decorative.")
    caption = CharBlock(required=False)

    class Meta:
        template = 'wagtailnhsukfrontend/image.html'
