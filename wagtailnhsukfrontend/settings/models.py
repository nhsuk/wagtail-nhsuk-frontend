from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
)
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.models import Orderable


@register_setting
class HeaderSettings(ClusterableModel, BaseSetting):
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

    show_search = models.BooleanField(default=False)

    panels = [
        MultiFieldPanel([
            FieldPanel('service_name'),
            FieldPanel('service_long_name'),
            PageChooserPanel('service_link'),
            FieldPanel('transactional'),
        ], heading="Service"),
        MultiFieldPanel([
            PageChooserPanel('logo_link'),
            FieldPanel('logo_aria'),
        ], heading="Logo"),
        FieldPanel('show_search'),
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
        PageChooserPanel('page'),
    ]


@register_setting
class EmergencyAlert(ClusterableModel, BaseSetting):
    enabled = models.BooleanField(default=False)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    link_url = models.URLField(blank=True)
    link_label = models.CharField(max_length=255, blank=True)

    # Auto-updating field
    last_updated = models.DateTimeField(auto_now=True)

    panels = [
        FieldPanel('enabled'),
        FieldPanel('title'),
        FieldPanel('description'),
        MultiFieldPanel([
            FieldPanel('link_url'),
            FieldPanel('link_label'),
        ], heading="Link"),
    ]
