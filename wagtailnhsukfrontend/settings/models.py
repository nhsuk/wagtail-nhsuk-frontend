from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.images import get_image_model_string

from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.models import Orderable


@register_setting
class HeaderSettings(ClusterableModel, BaseSiteSetting):
    service_name = models.CharField(max_length=255, blank=True)
    service_long_name = models.BooleanField(default=False)
    service_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='service_link',
    )

    transactional = models.BooleanField(default=False)

    logo_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    logo_aria = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Aria label override for the NHS logo."
    )
    logo_custom = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    show_search = models.BooleanField(default=False)

    organisation_name = models.CharField(max_length=255, blank=True)
    organisation_split_name = models.CharField(max_length=255, blank=True, help_text="Some NHS organisations’ names are too long to fit onto a single line and they have to run onto two lines. You should use discretion to decide where best to split your name depending on what makes most sense and what looks visually balanced.")
    organisation_descriptor = models.CharField(max_length=255, blank=True)
    organisation_white = models.BooleanField(default=False, help_text="Organisational header with a white background variant.")

    panels = [
        MultiFieldPanel([
            FieldPanel('logo_link'),
            FieldPanel('logo_aria'),
            FieldPanel('logo_custom'),
            FieldPanel('show_search'),
        ], heading="General"),
        MultiFieldPanel([
            FieldPanel('service_name'),
            FieldPanel('service_long_name'),
            FieldPanel('service_link'),
            FieldPanel('transactional'),
        ], heading="Service header"),
        MultiFieldPanel([
            FieldPanel('organisation_name'),
            FieldPanel('organisation_split_name'),
            FieldPanel('organisation_descriptor'),
            FieldPanel('organisation_white'),
        ], heading="Organisational header"),
        InlinePanel('navigation_links', heading="Navigation"),
    ]


class NavigationLink(Orderable):
    setting = ParentalKey(
        HeaderSettings,
        on_delete=models.CASCADE,
        related_name='navigation_links',
    )
    label = models.CharField(max_length=255)
    page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        FieldPanel('label'),
        FieldPanel('page'),
    ]


@register_setting
class FooterSettings(ClusterableModel, BaseSiteSetting):
    panels = [
        InlinePanel(
            'footer_links',
            label="Footer Links",
            help_text="There is a minimum of 1 link and a maximum of 9 ",
            min_num=1,
            max_num=9
        )
    ]


class FooterLinks(Orderable):

    setting = ParentalKey(
        FooterSettings,
        on_delete=models.CASCADE,
        related_name='footer_links',
    )
    link_url = models.URLField(blank=True)
    link_label = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('link_url'),
        FieldPanel('link_label'),
    ]


@register_setting
class FooterSettingsColumns(ClusterableModel, BaseSiteSetting):
    COLUMN_CHOICES = [
        (1, 'Column 1'),
        (2, 'Column 2'),
        (3, 'Column 3'),
        (4, 'Column 4'),
    ]

    enable_column_footer = models.BooleanField(
        default=False,
        help_text="Enable the column-based footer layout"
    )

    panels = [
        FieldPanel('enable_column_footer'),
        InlinePanel(
            'column_links',
            label="Footer Column Links",
            help_text="Add menu items and assign them to columns",
            min_num=1,
        )
    ]

class FooterColumnLinks(Orderable):
    setting = ParentalKey(
        FooterSettingsColumns,
        on_delete=models.CASCADE,
        related_name='column_links',
    )
    column = models.IntegerField(
        choices=FooterSettingsColumns.COLUMN_CHOICES,
        default=1
    )
    link_label = models.CharField(max_length=250)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    link_url = models.URLField(blank=True)

    panels = [
        FieldPanel('column'),
        FieldPanel('link_label'),
        FieldPanel('link_page'),
        FieldPanel('link_url'),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        return self.link_url