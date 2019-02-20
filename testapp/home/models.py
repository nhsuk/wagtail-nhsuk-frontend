from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import (
    ActionLinkBlock,
    CareCardBlock,
    WarningCalloutBlock,
    BackLinkBlock,
    ReviewDateBlock,
    HintTextBlock,
    DetailsBlock,
    GroupExpanderBlock,
    ExpanderBlock,
)


class HomePage(Page):

    parent_page_types = ['wagtailcore.Page']

    body = StreamField([
        ('action_link', ActionLinkBlock()),
        ('care_card', CareCardBlock()),
        ('warning_callout', WarningCalloutBlock()),
        ('back_link', BackLinkBlock()),
        ('review_date', ReviewDateBlock()),
        ('hint_text', HintTextBlock()),
        ('details', DetailsBlock()),
        ('expander', ExpanderBlock()),
        ('group_expander', GroupExpanderBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class ChildPage(Page):
    pass
