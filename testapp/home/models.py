from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtailnhsukfrontend.mixins import (
    HeroMixin,
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
    GreyPanelBlock,
    InsetTextBlock,
    ImageBlock,
    PanelBlock,
    PanelListBlock,
    RichTextBlock,
    StructBlock,
    WarningCalloutBlock,
    FlattenValueContext
)


class SectionTextBlock(FlattenValueContext, StructBlock):
    Section_text = RichTextBlock(
            features=['h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'hr', 'ol', 'ul', 'link', 'document-link'],
            label='Section Text'
    )
    class Meta:
        template = 'section_text.html'


class HomePage(HeroMixin, ReviewDateMixin, Page):

    parent_page_types = ['wagtailcore.Page']


    body = StreamField([
        ('action_link', ActionLinkBlock()),
        ('care_card', CareCardBlock()),
        ('section_text', SectionTextBlock()),
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
