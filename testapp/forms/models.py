from .forms import BigForm

from wagtail.models import Page


class FormPage(Page):

    parent_page_types = ['home.HomePage']

    def get_context(self, request):
        context = super().get_context(request)
        context['form'] = BigForm(request.POST or None)
        return context
