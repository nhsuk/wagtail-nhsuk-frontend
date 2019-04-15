from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.mixins import (
    ReviewDateMixin,
)

from wagtailnhsukfrontend.blocks import (
    ActionLinkBlock,
    CareCardBlock,
    DetailsBlock,
    DoBlock,
    DontBlock,
    ExpanderBlock,
    ExpanderGroupBlock,
    InsetTextBlock,
    ImageBlock,
    PanelBlock,
    WarningCalloutBlock,
    PromoBlock,
    PromoGroupBlock,
)


class HomePage(Page, ReviewDateMixin):

    parent_page_types = ['wagtailcore.Page']

    body = StreamField([
        ('action_link', ActionLinkBlock()),
        ('care_card', CareCardBlock()),
        ('details', DetailsBlock()),
        ('do_list', DoBlock()),
        ('dont_list', DontBlock()),
        ('expander', ExpanderBlock()),
        ('expander_group', ExpanderGroupBlock()),
        ('inset_text', InsetTextBlock()),
        ('image', ImageBlock()),
        ('panel', PanelBlock()),
        ('warning_callout', WarningCalloutBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    settings_panels = Page.settings_panels + ReviewDateMixin.settings_panels


class ChildPage(Page):
    pass


class PaginationPage(Page):
    """
    A page type to show the pagination component usage
    """


class HubsPage(Page):

    body = StreamField([
        ('promo', PromoBlock()),
        ('promo_group', PromoGroupBlock()),
    ])
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
