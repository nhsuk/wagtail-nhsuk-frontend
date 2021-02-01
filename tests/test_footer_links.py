from bs4 import BeautifulSoup
from django.test import Client
import pytest


@pytest.mark.django_db
def test_footer_links(db, django_db_setup, client: Client):
    response = client.get('/')
    soup = BeautifulSoup(response.content, 'html.parser')
    footer_links = soup.select('.nhsuk-footer__list-item')

    a_tag_external_link = footer_links[0].select_one('a')
    assert a_tag_external_link['href'] == 'http://www.nhs.uk'
    assert a_tag_external_link.text == 'NHS Website'

    a_tag_internal_link_using_alternative_title = footer_links[1].select_one('a')
    assert a_tag_internal_link_using_alternative_title['href'] == '/promo-hub/'
    assert a_tag_internal_link_using_alternative_title.text == 'Card Examples'

    a_tag_internal_link_using_page_title = footer_links[2].select_one('a')
    assert a_tag_internal_link_using_page_title['href'] == '/'
    assert a_tag_internal_link_using_page_title.text == 'Home'