from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from wagtailnhsukfrontend.blocks import (
    ActionLinkBlock,
    CardBasicBlock,
    CardClickableBlock,
    CardFeatureBlock,
    CardGroupBlock,
    CardImageBlock,
    CareCardBlock,
    DetailsBlock,
    DoBlock,
    DontBlock,
    ExpanderBlock,
    ExpanderGroupBlock,
    ImageBlock,
    InsetTextBlock,
    SummaryListBlock,
    WarningCalloutBlock,
)
from wagtailnhsukfrontend.mixins import HeroMixin, ReviewDateMixin


class HomePage(HeroMixin, ReviewDateMixin, Page):
    parent_page_types = ["wagtailcore.Page"]

    body = StreamField(
        [
            ("action_link", ActionLinkBlock()),
            ("care_card", CareCardBlock()),
            ("details", DetailsBlock()),
            ("do_list", DoBlock()),
            ("dont_list", DontBlock()),
            ("expander", ExpanderBlock()),
            ("expander_group", ExpanderGroupBlock()),
            ("feature_card", CardFeatureBlock()),
            ("inset_text", InsetTextBlock()),
            ("image", ImageBlock()),
            ("warning_callout", WarningCalloutBlock()),
            ("summary_list", SummaryListBlock()),
        ],
        use_json_field=True,
    )

    content_panels = (
        Page.content_panels
        + HeroMixin.content_panels
        + [
            FieldPanel("body"),
        ]
    )

    settings_panels = Page.settings_panels + ReviewDateMixin.settings_panels


class ChildPage(Page):
    pass


class PaginationPage(Page):
    """
    A page type to show the pagination component usage
    """


class HubsPage(Page):
    body = StreamField(
        [
            ("card_basic", CardBasicBlock()),
            ("card_clickable", CardClickableBlock()),
            ("card_image", CardImageBlock()),
            ("card_feature", CardFeatureBlock()),
            ("card_group", CardGroupBlock()),
        ],
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
