from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (3, 0):
    from wagtail.admin.panels import StreamFieldPanel
    from wagtail.models import Page
    from wagtail.fields import StreamField
else:
    from wagtail.admin.edit_handlers import StreamFieldPanel
    from wagtail.core.models import Page
    from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.mixins import (
    HeroMixin,
    ReviewDateMixin,
)

from wagtailnhsukfrontend.blocks import (
    ActionLinkBlock,
    CardBasicBlock,
    CardClickableBlock,
    CardImageBlock,
    CardFeatureBlock,
    CardGroupBlock,
    CareCardBlock,
    DetailsBlock,
    DoBlock,
    DontBlock,
    ExpanderBlock,
    ExpanderGroupBlock,
    InsetTextBlock,
    ImageBlock,
    WarningCalloutBlock,
    SummaryListBlock,
)


class HomePage(HeroMixin, ReviewDateMixin, Page):

    parent_page_types = ['wagtailcore.Page']

    body = StreamField([
        ('action_link', ActionLinkBlock()),
        ('care_card', CareCardBlock()),
        ('details', DetailsBlock()),
        ('do_list', DoBlock()),
        ('dont_list', DontBlock()),
        ('expander', ExpanderBlock()),
        ('expander_group', ExpanderGroupBlock()),
        ('feature_card', CardFeatureBlock()),
        ('inset_text', InsetTextBlock()),
        ('image', ImageBlock()),
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
        ('card_basic', CardBasicBlock()),
        ('card_clickable', CardClickableBlock()),
        ('card_image', CardImageBlock()),
        ('card_feature', CardFeatureBlock()),
        ('card_group', CardGroupBlock()),
    ])
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
