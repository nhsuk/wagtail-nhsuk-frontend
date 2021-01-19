from bs4 import BeautifulSoup
from django.test import Client
import pytest


@pytest.mark.django_db
def test_card_clickable_block_external_url(db, django_db_setup, client: Client):
    response = client.get('/promo-hub/')
    soup = BeautifulSoup(response.content, 'html.parser')
    a_tag = soup.select_one('.block-card_clickable:nth-of-type(2) a')

    assert a_tag['href'] == 'https://example.com/'


@pytest.mark.django_db
def test_card_clickable_block_internal_page(db, django_db_setup, client: Client):
    response = client.get('/promo-hub/')
    soup = BeautifulSoup(response.content, 'html.parser')
    a_tag = soup.select_one('.block-card_clickable:nth-of-type(3) a')

    assert a_tag['href'] == '/page-1/'
