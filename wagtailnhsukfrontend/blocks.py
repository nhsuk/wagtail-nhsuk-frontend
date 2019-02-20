from wagtail.core.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StructBlock,
    URLBlock,
    DateBlock,
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


class BackLinkBlock(StructBlock):

    link_title = CharBlock(default="Go Back", label="Go Back", required=True)
    back_url = URLBlock(label="Enter the back URL", required=True)

    class Meta:
        template = 'wagtailnhsukfrontend/back_link.html'


class ReviewDateBlock(StructBlock):

    reviewed_date = DateBlock(label="Enter the reviewed date", required=True,)
    last_review_label = CharBlock(default="Last review date: ", label="Last review date:", required=False)

    next_review_date = DateBlock(label="Enter the next review date", required=False)
    next_review_label = CharBlock(default="Next review due: ", label="Next review due:", required=False)

    class Meta:
        template = 'wagtailnhsukfrontend/review_date.html'


class HintTextBlock(StructBlock):

    hint_text = CharBlock(label="Hint Text", required=True)

    class Meta:
        template = 'wagtailnhsukfrontend/hint_text.html'


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
