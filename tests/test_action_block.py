from bs4 import BeautifulSoup
from django.core.exceptions import ValidationError
from django.test import Client
import pytest
from wagtailnhsukfrontend.blocks import ActionLinkBlock


@pytest.mark.django_db
def test_action_block_external_url(db, django_db_setup, client: Client):
    response = client.get('/')
    soup = BeautifulSoup(response.content, 'html.parser')
    a_tag = soup.select_one('.block-action_link:nth-of-type(1) a')
    span_tag = a_tag.select_one('span.nhsuk-action-link__text')

    assert a_tag['href'] == 'https://example.com'
    assert span_tag.text == 'Action Link External URL'


@pytest.mark.django_db
def test_action_block_internal_page(db, django_db_setup, client: Client):
    response = client.get('/')
    soup = BeautifulSoup(response.content, 'html.parser')
    a_tag = soup.select_one('.block-action_link:nth-of-type(2) a')
    span_tag = a_tag.select_one('span.nhsuk-action-link__text')

    assert a_tag['href'] == '/page-1/'
    assert span_tag.text == 'Action Link Internal Page'


def test_action_block_clean_one_link():
    block = ActionLinkBlock()
    value = {'text': 'testing', 'external_url': 'https://example.com/', 'new_window': False}
    clean_value = block.clean(value)

    assert value == clean_value
    

def test_action_block_clean_no_links():
    block = ActionLinkBlock()
    value = {'text': 'testing', 'external_url': None, 'internal_page': None, 'new_window': False}
    internal_error_message = '<ul class="errorlist"><li>Please choose a page or enter a URL above.</li></ul>'
    external_error_message = '<ul class="errorlist"><li>Please enter a URL or choose a page below.</li></ul>'
    
    with pytest.raises(ValidationError) as excinfo:
        clean_value = block.clean(value)

    assert str(excinfo.value.params['internal_page']) == internal_error_message
    assert str(excinfo.value.params['external_url']) == external_error_message
    assert "['Validation error in ActionLinkBlock']" == str(excinfo.value)


def test_action_block_clean_two_links():
    block = ActionLinkBlock()
    value = {'text': 'testing', 'external_url': 'https://example.com/', 
            'internal_page': 'https://internal.com/', 'new_window': False}
    error_message = '<ul class="errorlist"><li>Please only enter a URL or choose a page.</li></ul>'

    with pytest.raises(ValidationError) as excinfo:
        clean_value = block.clean(value)
    
    assert str(excinfo.value.params['internal_page']) == error_message
    assert str(excinfo.value.params['external_url']) == error_message
    assert "['Validation error in ActionLinkBlock']" == str(excinfo.value)