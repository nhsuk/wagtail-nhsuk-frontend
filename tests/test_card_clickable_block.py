import pytest
from django.core.exceptions import ValidationError

from wagtailnhsukfrontend.blocks import CardClickableBlock


def test_card_clickable_block_clean_one_link():
    block = CardClickableBlock()
    value = {"url": "https://example.com/"}
    clean_value = block.clean(value)

    assert value == clean_value


def test_card_clickable_block_clean_no_links():
    block = CardClickableBlock()
    value = {"url": None, "internal_page": None}
    internal_error_message = "Please choose a page or enter a URL below."
    external_error_message = "Please enter a URL or choose a page above."

    with pytest.raises(ValidationError) as excinfo:
        block.clean(value)

    assert internal_error_message in excinfo.value.params["internal_page"]
    assert external_error_message in excinfo.value.params["url"]
    assert excinfo.value.message == "Validation error in CardClickableBlock"


def test_card_clickable_block_clean_two_links():
    block = CardClickableBlock()
    value = {"url": "https://example.com/", "internal_page": "https://internal.com/"}
    error_message = "Please only enter a URL or choose a page."

    with pytest.raises(ValidationError) as excinfo:
        block.clean(value)

    assert error_message in excinfo.value.params["internal_page"]
    assert error_message in excinfo.value.params["url"]
    assert excinfo.value.message == "Validation error in CardClickableBlock"
