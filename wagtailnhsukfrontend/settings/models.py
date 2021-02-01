from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.forms import WagtailAdminModelForm
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


class FooterSettingsForm(WagtailAdminModelForm):
    def clean(self):
        cleaned_data = super().clean()        

        for link_form in self.formsets['footer_links'].forms:
            if link_form.is_valid():
                data = link_form.clean()
                if (data['link_url'] and data['internal_page']) or \
                    (not data['link_url'] and not data['internal_page']):
                    link_form.add_error('link_url', 'Either add a link url or choose a page to link to')
                    link_form.add_error('internal_page', 'Either add a link url or choose a page to link to')
                elif data['link_url'] and not data['link_label']:
                    link_form.add_error('link_label','Link label is required when adding a link url')

        return cleaned_data


@register_setting
class FooterSettings(ClusterableModel, BaseSetting):

    fixed_coloumn_footer = models.BooleanField(
        default=False,
        help_text="Enable this setting to change way the footer is styled, so links group into coloumns"
    )

    panels = [
        FieldPanel('fixed_coloumn_footer'),
        InlinePanel(
            'footer_links',
            label="Footer Links",
            help_text="There is a minimum of 1 link and a maximum of 9 ",
            min_num=1,
            max_num=9
        )
    ]

    base_form_class = FooterSettingsForm


class FooterLinks(Orderable):

    setting = ParentalKey(
        FooterSettings,
        on_delete=models.CASCADE,
        related_name='footer_links',
    )
    link_url = models.URLField(
        blank=True,
        help_text="If you add a link url then also enter the text for the link below"
    )
    link_label = models.CharField(
        blank=True,
        max_length=250,
        help_text="Link label is required if you enter a link url but is optional if you choose a page below")
    internal_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="If you are not adding an external URL choose a page to link to"
    )

    panels = [
        FieldPanel('link_url'),
        FieldPanel('link_label'),
        PageChooserPanel('internal_page'),
    ]
