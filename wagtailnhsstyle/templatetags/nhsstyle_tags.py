from django import template
from django.apps import apps
from wagtailnhsstyle.models import HeaderSettings

register = template.Library()


@register.inclusion_tag('wagtailnhsstyle/breadcrumb.html', takes_context=True)
def breadcrumbs(context):
    """
    Generates an array of pages which are passed to the breadcrumb template.
    """
    page = context['page']
    site = page.get_site()
    breadcrumb_pages = []

    # Traverse the page parents with get_parent() until we hit a site root
    while page.id != site.root_page_id and not page.is_root():
        page = page.get_parent()
        breadcrumb_pages = [page] + breadcrumb_pages

    return {
        'breadcrumb_pages': breadcrumb_pages,
    }


@register.inclusion_tag('wagtailnhsstyle/header.html', takes_context=True)
def header_from_settings(context, model_path):
    page = context['page']
    site = page.get_site()
    settings_model = apps.get_model(model_path)

    if not issubclass(settings_model, HeaderSettings):
        raise Exception("header setting model must inherit from wagtailnhsstyle.settings.HeaderSettings")

    header = settings_model.for_site(site)

    return {
        'service_name': header.service_name,
        'service_href': header.service_link.relative_url(site) if header.service_link else '',
        'service_long_name': header.service_long_name,
        'transactional': header.transactional,
        'logo_href': header.logo_link.relative_url(site) if header.logo_link else '',
        'logo_aria': header.logo_aria,
        'show_search': header.show_search,
        'primary_links' : [
            {
                'label': link.label,
                'url': link.page.relative_url(site)
            }
            for link in header.navigation_links.all()
        ],
    }
