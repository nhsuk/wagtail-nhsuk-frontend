from bs4 import BeautifulSoup
from django.test import Client
import pytest


@pytest.mark.django_db
def test_action_block(db, django_db_setup, client: Client):
    response = client.get('/')
    soup = BeautifulSoup(response.content, 'html.parser')
    a_tag = soup.select_one('a.nhsuk-action-link__link')
    span_tag = a_tag.select_one('span.nhsuk-action-link__text')

    assert a_tag['href'] == 'https://example.com'
    assert span_tag.text == 'Action Link'
