from django import template
from wagtailnhsukfrontend.settings.models import HeaderSettings

register = template.Library()


@register.inclusion_tag('wagtailnhsukfrontend/header.html', takes_context=True)
def header(context):
    page = context['page']
    site = page.get_site()
    header = HeaderSettings.for_site(site)

    return {
        'service_name': header.service_name,
        'service_href': header.service_link.relative_url(site) if header.service_link else '',
        'service_long_name': header.service_long_name,
        'transactional': header.transactional,
        'logo_href': header.logo_link.relative_url(site) if header.logo_link else '',
        'logo_aria': header.logo_aria,
        'show_search': header.show_search,
        'primary_links': [
            {
                'label': link.label,
                'url': link.page.relative_url(site)
            }
            for link in header.navigation_links.all()
        ],
    }
