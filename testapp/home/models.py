from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.mixins import (
    HeroMixin,
    ReviewDateMixin,
)

from wagtailnhsukfrontend.blocks import (
    ActionLinkBlock,
    CardBlock,
    CareCardBlock,
    DetailsBlock,
    DoBlock,
    DontBlock,
    ExpanderBlock,
    ExpanderGroupBlock,
    GreyPanelBlock,
    InsetTextBlock,
    ImageBlock,
    PanelBlock,
    PanelListBlock,
    WarningCalloutBlock,
    PromoBlock,
    PromoGroupBlock,
    SummaryListBlock,
)


class HomePage(HeroMixin, ReviewDateMixin, Page):

    parent_page_types = ['wagtailcore.Page']

    body = StreamField([
        ('action_link', ActionLinkBlock()),
        ('card_block', CardBlock()),
        ('care_card', CareCardBlock()),
        ('details', DetailsBlock()),
        ('do_list', DoBlock()),
        ('dont_list', DontBlock()),
        ('expander', ExpanderBlock()),
        ('expander_group', ExpanderGroupBlock()),
        ('inset_text', InsetTextBlock()),
        ('image', ImageBlock()),
        ('panel', PanelBlock()),
        ('panel_list', PanelListBlock()),
        ('grey_panel', GreyPanelBlock()),
        ('warning_callout', WarningCalloutBlock()),
        ('summary_list', SummaryListBlock()),
    ])

    content_panels = Page.content_panels + HeroMixin.content_panels + [
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
