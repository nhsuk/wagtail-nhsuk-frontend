import pytest
from wagtail.models import Page

from wagtailnhsukfrontend.templatetags.nhsukfrontend_tags import breadcrumb


def get_breadcrumb_context(page):
    """Get the breadcrumb context that will be passed to the breadcrumb template."""
    fake_context = {
        "page": page,
    }
    # The breadcrumb tag is an inclusion_tag which returns a new context.
    new_context = breadcrumb(fake_context)
    return new_context["breadcrumb_pages"]


def get_level_2_breadcrumb():
    """Get the breadcrumb context for a 2-levels-deep page."""
    page = Page.objects.get(url_path="/home/page-1/page-2/")
    return get_breadcrumb_context(page)


def get_level_1_breadcrumb():
    """Get the breadcrumb context for a 1-level deep page."""
    page = Page.objects.get(url_path="/home/page-1/")
    return get_breadcrumb_context(page)


def get_homepage_breadcrumb():
    """Get the breadcrumb context for a root page."""
    page = Page.objects.get(url_path="/home/")
    return get_breadcrumb_context(page)


@pytest.mark.django_db
def test_level_2_breadcrumb_length(db, django_db_setup):
    breadcrumb_pages = get_level_2_breadcrumb()

    assert len(breadcrumb_pages) == 2


@pytest.mark.django_db
def test_level_2_breadcrumb_pages(db, django_db_setup):
    breadcrumb_pages = get_level_2_breadcrumb()

    homepage = Page.objects.get(url_path="/home/")
    page1 = Page.objects.get(url_path="/home/page-1/")

    assert breadcrumb_pages[0] == homepage
    assert breadcrumb_pages[1] == page1


@pytest.mark.django_db
def test_level_1_breadcrumb_length(db, django_db_setup):
    breadcrumb_pages = get_level_1_breadcrumb()

    assert len(breadcrumb_pages) == 1


@pytest.mark.django_db
def test_level_1_breadcrumb_pages(db, django_db_setup):
    breadcrumb_pages = get_level_1_breadcrumb()

    homepage = Page.objects.get(url_path="/home/")

    assert breadcrumb_pages[0] == homepage
