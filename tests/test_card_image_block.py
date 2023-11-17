import pytest
from django.core.exceptions import ValidationError

from wagtailnhsukfrontend.blocks import CardImageBlock


def test_card_image_block_clean_one_link():
    block = CardImageBlock()
    value = {"url": "https://example.com/"}
    clean_value = block.clean(value)

    assert value == clean_value


def test_card_image_block_clean_no_links():
    block = CardImageBlock()
    value = {}
    clean_value = block.clean(value)

    assert value == clean_value


def test_card_image_block_clean_two_links():
    block = CardImageBlock()
    value = {"url": "https://example.com/", "internal_page": "https://internal.com/"}
    error_message = "Please only enter a URL or choose a page."

    with pytest.raises(ValidationError) as excinfo:
        block.clean(value)

    assert error_message in excinfo.value.params["internal_page"]
    assert error_message in excinfo.value.params["url"]
    assert excinfo.value.message == "Validation error in CardImageBlock"
