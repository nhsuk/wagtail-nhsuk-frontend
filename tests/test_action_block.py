from bs4 import BeautifulSoup
from django.test import Client
import pytest


@pytest.mark.django_db
def test_action_block_external_url(db, django_db_setup, client: Client):
    response = client.get('/')
    soup = BeautifulSoup(response.content, 'html.parser')
    a_tag = soup.select_one('a.nhsuk-action-link__link.external-url')
    span_tag = a_tag.select_one('span.nhsuk-action-link__text')

    assert a_tag['href'] == 'https://example.com'
    assert span_tag.text == 'Action Link (external url)'


@pytest.mark.django_db
def test_action_block_page_chooser(db, django_db_setup, client: Client):
    response = client.get('/')
    soup = BeautifulSoup(response.content, 'html.parser')
    a_tag = soup.select_one('a.nhsuk-action-link__link.internal-page')
    span_tag = a_tag.select_one('span.nhsuk-action-link__text')

    assert a_tag['href'] == '/page-1/'
    assert span_tag.text == 'Action Link (internal page)'
