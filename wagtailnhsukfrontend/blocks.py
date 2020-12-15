from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
    ChoiceBlock,
    IntegerBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    URLBlock,
    ListBlock,
)
from wagtail.core.blocks.field_block import PageChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList


class FlattenValueContext:
    """NHS.UK StructBlock mixin that flattens `value` for re-usability of templates"""

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context.update(value)
        return context


class ActionLinkBlock(FlattenValueContext, StructBlock):

    text = CharBlock(label="Link text", required=True)
    internal_page = PageChooserBlock(label="Internal Page", required=False)
    external_url = URLBlock(label="URL", required=False)
    new_window = BooleanBlock(required=False, label="Open URL in new window")

    class Meta:
        icon = 'link'
        template = 'wagtailnhsukfrontend/action_link.html'
        help_text = 'Action link requires an Internal page selected or a URL entered'

    def clean(self, value):

        errors = {}

        url_links = 0

        if value.get('external_url'):
            url_links += 1
        if value.get('internal_page'):
            url_links += 1

        if not url_links:
            errors['internal_page'] = ErrorList(['Please choose a page or enter a URL below.'])
            errors['external_url'] = ErrorList(['Please enter a URL or choose a page above.'])
        elif url_links > 1:
            errors['internal_page'] = ErrorList(['Please only enter a URL or choose a page.'])
            errors['external_url'] = ErrorList(['Please only enter a URL or choose a page.'])

        if errors:
            raise ValidationError('Validation error in ActionLinkBlock', params=errors)

        return super().clean(value)


class WarningCalloutBlock(FlattenValueContext, StructBlock):

    title = CharBlock(required=True, default='Important')
    heading_level = IntegerBlock(required=True, min_value=2, max_value=6, default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.')
    body = RichTextBlock(required=True)

    class Meta:
        icon = 'warning'
        template = 'wagtailnhsukfrontend/warning_callout.html'


class InsetTextBlock(FlattenValueContext, StructBlock):

    body = RichTextBlock(required=True)

    class Meta:
        icon = 'warning'
        template = 'wagtailnhsukfrontend/inset_text.html'


class PanelBlock(FlattenValueContext, StructBlock):

    label = CharBlock(required=False)
    heading_level = IntegerBlock(min_value=2, max_value=6, default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.')
    body = RichTextBlock(required=True)

    class Meta:
        icon = 'doc-full'
        template = 'wagtailnhsukfrontend/panel.html'


class GreyPanelBlock(FlattenValueContext, StructBlock):

    label = CharBlock(label='heading', required=False)
    heading_level = IntegerBlock(min_value=2, max_value=6, default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.')
    body = RichTextBlock(required=True)

    class Meta:
        icon = 'doc-full-inverse'
        template = 'wagtailnhsukfrontend/grey_panel.html'


class PanelListBlock(FlattenValueContext, StructBlock):

    panels = ListBlock(StructBlock([
        ('left_panel', PanelBlock()),
        ('right_panel', PanelBlock()),
    ]))

    class Meta:
        icon = 'list-ul'
        template = 'wagtailnhsukfrontend/panel_list.html'


class DoBlock(FlattenValueContext, StructBlock):

    heading_level = IntegerBlock(required=True, min_value=2, max_value=6, default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.')
    label = CharBlock(label='Heading', required=False, help_text='Adding a label here will overwrite the default of Do')
    do = ListBlock(RichTextBlock)

    class Meta:
        icon = 'tick'
        template = 'wagtailnhsukfrontend/do_list.html'


class DontBlock(FlattenValueContext, StructBlock):

    heading_level = IntegerBlock(required=True, min_value=2, max_value=6, default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.')
    label = CharBlock(label='Heading', required=False, help_text='Adding a label here will overwrite the default of Don\'t')
    dont = ListBlock(RichTextBlock)

    class Meta:
        icon = 'cross'
        template = 'wagtailnhsukfrontend/dont_list.html'


class ImageBlock(FlattenValueContext, StructBlock):

    content_image = ImageChooserBlock(required=True)
    alt_text = CharBlock(required=False, help_text="Only leave this blank if the image is decorative.")
    caption = CharBlock(required=False)

    class Meta:
        icon = 'image'
        template = 'wagtailnhsukfrontend/image.html'


class BasePromoBlock(FlattenValueContext, StructBlock):

    internal_page = PageChooserBlock(label="Internal Page", required=False)
    url = URLBlock(label="URL", required=False)
    heading = CharBlock(required=True)
    description = CharBlock(required=False)
    content_image = ImageChooserBlock(label="Image", required=False)
    alt_text = CharBlock(required=False)

    class Meta:
        icon = 'pick'
        template = 'wagtailnhsukfrontend/promo.html'
        help_text = 'Promo requires an Internal page selected or a URL entered'

    def clean(self, value):

        errors = {}

        url_links = 0

        if value.get('url'):
            url_links += 1
        if value.get('internal_page'):
            url_links += 1

        if not url_links:
            errors['internal_page'] = ErrorList(['Please choose a page or enter a URL below.'])
            errors['url'] = ErrorList(['Please enter a URL or choose a page above.'])
        elif url_links > 1:
            errors['internal_page'] = ErrorList(['Please only enter a URL or choose a page.'])
            errors['url'] = ErrorList(['Please only enter a URL or choose a page.'])

        if errors:
            raise ValidationError('Validation error in ActionLinkBlock', params=errors)

        return super().clean(value)


class PromoBlock(BasePromoBlock):

    size = ChoiceBlock([
        ('', 'Default'),
        ('small', 'Small'),
    ], required=False)

    heading_level = IntegerBlock(min_value=2, max_value=6, default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.')

    class Meta:
        template = 'wagtailnhsukfrontend/promo.html'


class PromoGroupBlock(FlattenValueContext, StructBlock):

    column = ChoiceBlock([
        ('one-half', 'One-half'),
        ('one-third', 'One-third'),
    ], default='one-half', required=True)

    size = ChoiceBlock([
        ('', 'Default'),
        ('small', 'Small'),
    ], required=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context['num_columns'] = {
            'one-half': 2,
            'one-third': 3,
        }[value['column']]
        return context

    heading_level = IntegerBlock(min_value=2, max_value=6, default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.')

    promos = ListBlock(BasePromoBlock)

    class Meta:
        template = 'wagtailnhsukfrontend/promo_group.html'


class SummaryListRowBlock(StructBlock):

    key = CharBlock()

    value = RichTextBlock()


class SummaryListBlock(FlattenValueContext, StructBlock):

    rows = ListBlock(SummaryListRowBlock)
    no_border = BooleanBlock(default=False, required=False)

    class Meta:
        icon = 'form'
        template = 'wagtailnhsukfrontend/summary_list.html'


class DetailsBlock(FlattenValueContext, StructBlock):

    # Define a BodyStreamBlock class in this way to make it easier to subclass and add extra body blocks
    class BodyStreamBlock(StreamBlock):
        richtext = RichTextBlock()
        action_link = ActionLinkBlock()
        inset_text = InsetTextBlock()
        image = ImageBlock()
        panel = PanelBlock()
        warning_callout = WarningCalloutBlock()
        summary_list = SummaryListBlock()

    title = CharBlock(required=True)
    body = BodyStreamBlock(required=True)

    class Meta:
        icon = 'collapse-down'
        template = 'wagtailnhsukfrontend/details.html'


class ExpanderBlock(DetailsBlock):

    class BodyStreamBlock(StreamBlock):
        richtext = RichTextBlock()
        action_link = ActionLinkBlock()
        inset_text = InsetTextBlock()
        image = ImageBlock()
        grey_panel = GreyPanelBlock()
        warning_callout = WarningCalloutBlock()
        summary_list = SummaryListBlock()

    # We need to override the body since expanders can have grey_panels instead of regular panels
    body = BodyStreamBlock(required=True)

    class Meta:
        icon = 'plus-inverse'
        template = 'wagtailnhsukfrontend/expander.html'


class ExpanderGroupBlock(FlattenValueContext, StructBlock):

    expanders = ListBlock(ExpanderBlock)

    class Meta:
        icon = 'plus-inverse'
        template = 'wagtailnhsukfrontend/expander_group.html'


class CareCardBlock(FlattenValueContext, StructBlock):

    type = ChoiceBlock([
        ('primary', 'Non-urgent'),
        ('urgent', 'Urgent'),
        ('immediate', 'Immediate'),
    ], required=True, default='primary',)
    heading_level = IntegerBlock(required=True, min_value=2, max_value=6, default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.')
    title = CharBlock(required=True)

    class BodyStreamBlock(StreamBlock):
        richtext = RichTextBlock()
        action_link = ActionLinkBlock()
        details = DetailsBlock()
        inset_text = InsetTextBlock()
        image = ImageBlock()
        grey_panel = GreyPanelBlock()
        warning_callout = WarningCalloutBlock()
        summary_list = SummaryListBlock()

    body = BodyStreamBlock(required=True)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context['accessible_title_prefix'] = {
            'primary': 'Non-urgent advice: ',
            'urgent': 'Urgent advice:',
            'immediate': 'Immediate action required:',
        }[value['type']]
        return context

    class Meta:
        icon = 'help'
        template = 'wagtailnhsukfrontend/care_card.html'
