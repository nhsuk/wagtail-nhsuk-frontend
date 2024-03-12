import pytest
from django.test.client import Client
from wagtailnhsukfrontend.templatetags.nhsukfrontend_tags import pagination

from wagtail.models import Page


client = Client()


def get_pagination_context(page, request):
    """Get the pagination context that will be passed to the pagination template."""
    fake_context = {"page": page, "request": request}
    # The pagination tag is an inclusion_tag which returns a new context.
    new_context = pagination(fake_context)
    return new_context


def get_pagination_page_context(number):
    """ Get paginated page """
    response = client.get(f"/home/pagination/pagination-page-{number}/")
    request = response.wsgi_request
    page = Page.objects.get(url_path=f"/home/pagination/pagination-page-{number}/")
    return get_pagination_context(page, request)


@pytest.mark.django_db
def test_first_page(db, django_db_setup):
    """ Check first page has next keys but no prev keys """
    context = get_pagination_page_context(1)
    expected = {
        "next_label": "Pagination page 2",
        "next_url": "/pagination/pagination-page-2/",
    }
    assert context == expected


@pytest.mark.django_db
def test_third_page(db, django_db_setup):
    """ Check third page has next and prev keys """
    context = get_pagination_page_context(3)
    expected = {
        "prev_label": "Pagination page 2",
        "prev_url": "/pagination/pagination-page-2/",
        "next_label": "Pagination page 4",
        "next_url": "/pagination/pagination-page-4/",
    }
    assert context == expected


@pytest.mark.django_db
def test_final_page(db, django_db_setup):
    """ Check fourth page has only prev keys """
    context = get_pagination_page_context(4)
    print(context)
    expected = {
        "prev_label": "Pagination page 3",
        "prev_url": "/pagination/pagination-page-3/",
    }
    assert context == expected
