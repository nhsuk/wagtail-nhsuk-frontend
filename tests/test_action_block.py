from bs4 import BeautifulSoup
from django.core.exceptions import ValidationError
from django.test import Client
import pytest
from wagtail.models import Page
from wagtailnhsukfrontend.blocks import ActionLinkBlock, CareCardBlock


@pytest.mark.django_db
def test_action_block_external_url(db, django_db_setup, client: Client):
    response = client.get("/")
    soup = BeautifulSoup(response.content, "html.parser")
    a_tag = soup.select_one(".block-action_link:nth-of-type(1) a")
    span_tag = a_tag.select_one("span.nhsuk-action-link__text")

    assert a_tag["href"] == "https://example.com"
    assert span_tag.text == "Action Link External URL"


@pytest.mark.django_db
def test_action_block_internal_page(db, django_db_setup, client: Client):
    response = client.get("/")
    soup = BeautifulSoup(response.content, "html.parser")
    a_tag = soup.select_one(".block-action_link:nth-of-type(2) a")
    span_tag = a_tag.select_one("span.nhsuk-action-link__text")

    assert a_tag["href"] == "/page-1/"
    assert span_tag.text == "Action Link Internal Page"


def test_action_block_clean_one_link():
    block = ActionLinkBlock()
    value = {
        "text": "testing",
        "external_url": "https://example.com/",
        "new_window": False,
    }
    clean_value = block.clean(value)

    assert value == clean_value


def test_action_block_clean_no_links():
    block = ActionLinkBlock()
    value = {
        "text": "testing",
        "external_url": None,
        "internal_page": None,
        "new_window": False,
    }
    internal_error_message = "Please choose a page or enter a URL above."
    external_error_message = "Please enter a URL or choose a page below."

    with pytest.raises(ValidationError) as excinfo:
        block.clean(value)

    assert internal_error_message in excinfo.value.params["internal_page"]
    assert external_error_message in excinfo.value.params["external_url"]
    assert excinfo.value.message == "Validation error in ActionLinkBlock"


def test_action_block_clean_two_links():
    block = ActionLinkBlock()
    value = {
        "text": "testing",
        "external_url": "https://example.com/",
        "internal_page": "https://internal.com/",
        "new_window": False,
    }
    error_message = "Please only enter a URL or choose a page."

    with pytest.raises(ValidationError) as excinfo:
        block.clean(value)

    assert error_message in excinfo.value.params["internal_page"]
    assert error_message in excinfo.value.params["external_url"]
    assert excinfo.value.message == "Validation error in ActionLinkBlock"


@pytest.mark.django_db
def test_action_link_reversed_in_emergency_care_card():
    block = CareCardBlock()

    value = block.to_python({
        "type": "immediate",
        "heading_level": 3,
        "title": "Immediate!",
        "body": [
            {
                "type": "action_link",
                "value": {
                    "text": "Emergency action",
                    "external_url": "https://example.com/",
                    "new_window": False,
                    "internal_page": None,
                },
            }
        ],
    })

    cleaned = block.clean(value)

    html = block.render(cleaned)

    assert 'class="nhsuk-action-link nhsuk-action-link--reverse"' in html


@pytest.mark.django_db
def test_action_link_not_reversed_in_primary_care_card():
    block = CareCardBlock()

    value = block.to_python({
        "type": "primary",
        "heading_level": 3,
        "title": "Non-urgent",
        "body": [
            {
                "type": "action_link",
                "value": {
                    "text": "Standard action",
                    "external_url": "https://example.com/",
                    "new_window": False,
                    "internal_page": None,
                },
            }
        ],
    })

    cleaned = block.clean(value)

    html = block.render(cleaned)

    assert 'class="nhsuk-action-link"' in html
    assert 'nhsuk-action-link--reverse' not in html


@pytest.mark.django_db
def test_action_link_internal_page_reversed_in_emergency_care_card():
    home = Page.objects.get(id=1)
    internal_page = home.add_child(
        instance=Page(title="Care card target", slug="care-card-target")
    )

    block = CareCardBlock()

    value = block.to_python({
        "type": "immediate",
        "heading_level": 3,
        "title": "Immediate!",
        "body": [
            {
                "type": "action_link",
                "value": {
                    "text": "Emergency internal action",
                    "external_url": None,
                    "new_window": False,
                    "internal_page": internal_page.id,
                },
            }
        ],
    })

    cleaned = block.clean(value)

    html = block.render(cleaned)

    assert f'href="{internal_page.url}"' in html
    assert 'class="nhsuk-action-link nhsuk-action-link--reverse"' in html
