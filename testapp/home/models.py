from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.blocks import (
    ActionLinkBlock,
    CareCardBlock,
    WarningCalloutBlock,
)


class HomePage(Page):

    parent_page_types = ['wagtailcore.Page']

    body = StreamField([
        ('action_link', ActionLinkBlock()),
        ('care_card', CareCardBlock()),
        ('warning_callout', WarningCalloutBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class ChildPage(Page):
    pass


class PaginationPage(Page):
    """
    A page type to show the pagination component usage
    """
