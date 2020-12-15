from bs4 import BeautifulSoup
from django.test import Client
import pytest


@pytest.mark.django_db
def test_promo_block_external_url(db, django_db_setup, client: Client):
    response = client.get('/promo-hub/')
    soup = BeautifulSoup(response.content, 'html.parser')
    a_tag = soup.select_one('a.nhsuk-promo__link-wrapper.external-url')

    assert a_tag['href'] == 'http://example.com/'



@pytest.mark.django_db
def test_promo_block_page_chooser(db, django_db_setup, client: Client):
    response = client.get('/promo-hub/')
    soup = BeautifulSoup(response.content, 'html.parser')
    a_tag = soup.select_one('a.nhsuk-promo__link-wrapper.internal-page')

    assert a_tag['href'] == '/page-1/'
