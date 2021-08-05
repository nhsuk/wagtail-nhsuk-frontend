from django.core.exceptions import ValidationError
from wagtailnhsukfrontend.blocks import CardClickableBlock
import pytest


def test_card_clickable_block_clean_one_link():
    block = CardClickableBlock()
    value = {"url": "https://example.com/"}
    clean_value = block.clean(value)

    assert value == clean_value


def test_card_clickable_block_clean_no_links():
    block = CardClickableBlock()
    value = {"url": None, "internal_page": None}
    internal_error_message = (
        '<ul class="errorlist"><li>Please choose a page or enter a URL below.</li></ul>'
    )
    external_error_message = (
        '<ul class="errorlist"><li>Please enter a URL or choose a page above.</li></ul>'
    )

    with pytest.raises(ValidationError) as excinfo:
        block.clean(value)

    assert str(excinfo.value.params["internal_page"]) == internal_error_message
    assert str(excinfo.value.params["url"]) == external_error_message
    assert "['Validation error in CardClickableBlock']" == str(excinfo.value)


def test_card_clickable_block_clean_two_links():
    block = CardClickableBlock()
    value = {"url": "https://example.com/", "internal_page": "https://internal.com/"}
    error_message = (
        '<ul class="errorlist"><li>Please only enter a URL or choose a page.</li></ul>'
    )

    with pytest.raises(ValidationError) as excinfo:
        block.clean(value)

    assert str(excinfo.value.params["internal_page"]) == error_message
    assert str(excinfo.value.params["url"]) == error_message
    assert "['Validation error in CardClickableBlock']" == str(excinfo.value)
