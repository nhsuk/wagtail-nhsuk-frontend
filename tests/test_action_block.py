from bs4 import BeautifulSoup
from django.test import Client
import pytest


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
