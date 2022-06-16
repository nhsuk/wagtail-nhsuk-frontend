from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (3, 0):
    from wagtail.models import Page
else:
    from wagtail.core.models import Page

from .forms import BigForm


class FormPage(Page):

    parent_page_types = ['home.HomePage']

    def get_context(self, request):
        context = super().get_context(request)
        context['form'] = BigForm(request.POST or None)
        return context
