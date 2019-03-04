from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import (
    ActionLinkBlock,
    CareCardBlock,
    WarningCalloutBlock,
    InsetTextBlock,
    DetailsBlock,
    ExpanderGroupBlock,
    ExpanderBlock,
    PanelBlock,
    DoDontBlock,
)


class HomePage(Page):

    parent_page_types = ['wagtailcore.Page']

    body = StreamField([
        ('action_link', ActionLinkBlock()),
        ('care_card', CareCardBlock()),
        ('warning_callout', WarningCalloutBlock()),
        ('inset_text', InsetTextBlock()),
        ('details', DetailsBlock()),
        ('expander', ExpanderBlock()),
        ('group_expander', ExpanderGroupBlock()),
        ('panel', PanelBlock()),
        ('do_and_dont_list', DoDontBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class ChildPage(Page):
    pass
