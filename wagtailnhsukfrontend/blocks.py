from wagtail.core.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StructBlock,
    URLBlock,
    ListBlock,
)


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

    details_title = CharBlock(label="Title", required=True)
    details_body = RichTextBlock(label="Body", required=True)

    class Meta:
        template = 'wagtailnhsukfrontend/details.html'


class ExpanderBlock(StructBlock):

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context['expander'] = ' nhsuk-expander'
        return context

    details_title = CharBlock(label="Title", required=True)
    details_body = RichTextBlock(label="Body", required=True)

    class Meta:
        template = 'wagtailnhsukfrontend/details.html'


class GroupExpanderBlock(StructBlock):

    expanders = ListBlock(ExpanderBlock)

    class Meta:
        template = 'wagtailnhsukfrontend/expander_group.html'
