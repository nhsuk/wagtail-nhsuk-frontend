import pytest
from django.test import RequestFactory
from wagtail.models import Page

from wagtailnhsukfrontend.templatetags.nhsukfrontend_tags import contents_list


def get_contents_list_context(page=None):
    """Get the contents_list context that will be passed to the template."""
    page = page or Page.objects.get(url_path="/home/pagination/pagination-page-1/")
    fake_context = {"page": page, "request": RequestFactory().get("/fake/url/")}
    # The contents_list tag is an inclusion_tag which returns a new context.
    new_context = contents_list(fake_context)
    return new_context


@pytest.mark.django_db
def test_contents_list_siblings_are_dicts(db, django_db_setup):
    template_context = get_contents_list_context()
    for item in template_context["links"]:
        assert isinstance(item, dict)


@pytest.mark.django_db
def test_contents_list_length(db, django_db_setup):
    template_context = get_contents_list_context()
    # length = 4 ensures that our unpublished page didn't appear
    assert len(template_context["links"]) == 4


@pytest.mark.django_db
def test_contents_list_is_current_page(db, django_db_setup):
    page = Page.objects.get(url_path="/home/pagination/pagination-page-3/")
    template_context = get_contents_list_context(page=page)
    assert template_context["links"][2]["is_current"] is True
    assert template_context["links"][3]["is_current"] is False


def test_contents_list_has_href(db, django_db_setup):
    template_context = get_contents_list_context()
    assert template_context["links"][0]["href"] == "/pagination/pagination-page-1/"


def test_contents_list_has_label(db, django_db_setup):
    template_context = get_contents_list_context()
    assert template_context["links"][0]["label"] == "Pagination page 1"
