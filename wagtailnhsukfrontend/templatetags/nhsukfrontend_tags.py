from django import template

register = template.Library()


@register.inclusion_tag('wagtailnhsukfrontend/breadcrumb.html', takes_context=True)
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


@register.inclusion_tag('wagtailnhsukfrontend/pagination.html', takes_context=True)
def pagination(context):
    """
    Calculates previous and next page values which are passed to the pagination template.
    """
    page = context['page']
    request = context['request']

    prev = page.get_prev_siblings().live().first()
    next = page.get_next_siblings().live().first()

    template_context = {}

    if prev:
        template_context['prev_label'] = prev.title
        template_context['prev_url'] = prev.get_url(request)
    if next:
        template_context['next_label'] = next.title
        template_context['next_url'] = next.get_url(request)

    return template_context
