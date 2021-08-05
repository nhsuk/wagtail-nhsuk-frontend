from django.core.exceptions import ValidationError
from wagtailnhsukfrontend.blocks import CardImageBlock
import pytest


def test_card_image_block_clean_one_link():
    block = CardImageBlock()
    value = {'url': 'https://example.com/'}
    clean_value = block.clean(value)

    assert value == clean_value
    

def test_card_image_block_clean_no_links():
    block = CardImageBlock()
    value = {}
    clean_value = block.clean(value)

    assert value == clean_value


def test_card_image_block_clean_two_links():
    block = CardImageBlock()
    value = {'url': 'https://example.com/', 
            'internal_page': 'https://internal.com/'}
    error_message = '<ul class="errorlist"><li>Please only enter a URL or choose a page.</li></ul>'

    with pytest.raises(ValidationError) as excinfo:
        clean_value = block.clean(value)
    
    assert str(excinfo.value.params['internal_page']) == error_message
    assert str(excinfo.value.params['url']) == error_message
    assert "['Validation error in CardImageBlock']" == str(excinfo.value)