from bs4 import BeautifulSoup
from django.test import Client
import pytest


@pytest.mark.django_db
def test_footer_links(db, django_db_setup, client: Client):
    response = client.get('/')
    soup = BeautifulSoup(response.content, 'html.parser')
    # a_tag = soup.select_one('.block-card_clickable:nth-of-type(2) a')

    # assert a_tag['href'] == 'https://example.com/'