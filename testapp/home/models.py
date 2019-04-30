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
    WarningCalloutBlock,
    FormBlock
)

from wagtailnhsukfrontend.forms.blocks import FormFieldBlock
from wagtailnhsukfrontend.forms.creator import FormCreator
from django.shortcuts import render

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


class FormPage(Page):
    body = StreamField([
        ('form', FormBlock()),
        ('action_link', ActionLinkBlock())
    ], default=[])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
    
    def serve(self, request): 
        if request.method == 'POST': 
            return super(FormPage, self).serve(request) 
        else: 
                # display the page as usual 
            return super(FormPage, self).serve(request) 



class TestFormPage(Page):
    body = StreamField([
        ('form', FormFieldBlock()),
        ('action_link', ActionLinkBlock())
    ], default=[])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
    
    def serve(self, request):

        if request.method == 'POST':
            form = FormCreator(request.POST, form_fields=self.body.stream_data[0].get('value'))
            if form.is_valid():
                flavour = form.cleaned_data
                return render(request, 'flavours/thankyou.html', {
                    'page': self,
                    'flavour': flavour,
                })
        else:
            form = FormCreator(form_fields=self.body.stream_data[0].get('value'))

        return render(request, '/home/lasercut/git/wagtail-nhsuk-frontend/testapp/home/templates/home/test_form_page.html', {
            'page': self,
            'form': form,
        })
