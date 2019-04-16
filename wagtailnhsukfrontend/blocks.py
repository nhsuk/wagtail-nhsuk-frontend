from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
    ChoiceBlock,
    IntegerBlock,
    RichTextBlock,
    StructBlock,
    URLBlock,
    ListBlock,
)
from wagtail.images.blocks import ImageChooserBlock


class ActionLinkBlock(StructBlock):

    text = CharBlock(label="Link text", required=True)
    external_url = URLBlock(label="URL", required=True)
    new_window = BooleanBlock(required=False, label="Open in new window")

    class Meta:
        template = 'wagtailnhsukfrontend/action_link.html'


class CareCardBlock(StructBlock):

    type = ChoiceBlock([
        ('primary', 'Non-urgent'),
        ('urgent', 'Urgent'),
        ('immediate', 'Immediate'),
    ], required=True, default='primary',)
    heading_level = IntegerBlock(required=True, min_value=2, max_value=4, default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.')
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


class WarningCalloutBlock(StructBlock):

    title = CharBlock(required=True, default='Important')
    heading_level = IntegerBlock(required=True, min_value=2, max_value=4, default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.')
    body = RichTextBlock(required=True)

    class Meta:
        template = 'wagtailnhsukfrontend/warning_callout.html'


class InsetTextBlock(StructBlock):

    body = RichTextBlock(required=True)

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

    label = CharBlock(required=False)
    heading_level = IntegerBlock(min_value=2, max_value=4, default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.')
    body = RichTextBlock(required=True)

    class Meta:
        template = 'wagtailnhsukfrontend/panel.html'


class GreyPanelBlock(StructBlock):

    label = CharBlock(label='heading', required=False)
    heading_level = IntegerBlock(min_value=2, max_value=4, default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.')
    body = RichTextBlock(required=True)

    class Meta:
        template = 'wagtailnhsukfrontend/grey_panel.html'


class PanelListBlock(StructBlock):

    panels = ListBlock(StructBlock([
        ('left_panel', PanelBlock()),
        ('right_panel', PanelBlock()),
    ]))

    class Meta:
        template = 'wagtailnhsukfrontend/panel_list.html'


class DoBlock(StructBlock):

    heading_level = IntegerBlock(required=True, min_value=2, max_value=4, default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.')

    do = ListBlock(RichTextBlock)

    class Meta:
        template = 'wagtailnhsukfrontend/do_list.html'


class DontBlock(StructBlock):

    heading_level = IntegerBlock(required=True, min_value=2, max_value=4, default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.')

    dont = ListBlock(RichTextBlock)

    class Meta:
        template = 'wagtailnhsukfrontend/dont_list.html'


class ImageBlock(StructBlock):

    content_image = ImageChooserBlock(required=True)
    alt_text = CharBlock(required=False, help_text="Only leave this blank if the image is decorative.")
    caption = CharBlock(required=False)

    class Meta:
        template = 'wagtailnhsukfrontend/image.html'
