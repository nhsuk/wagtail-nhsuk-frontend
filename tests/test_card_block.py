import pytest
from bs4 import BeautifulSoup
from django.test import Client


@pytest.mark.django_db
def test_card_clickable_block_external_url(db, django_db_setup, client: Client):
    response = client.get("/promo-hub/")
    soup = BeautifulSoup(response.content, "html.parser")
    a_tag = soup.select_one(".block-card_clickable:nth-of-type(2) a")

    assert a_tag["href"] == "https://example.com/"


@pytest.mark.django_db
def test_card_clickable_block_internal_page(db, django_db_setup, client: Client):
    response = client.get("/promo-hub/")
    soup = BeautifulSoup(response.content, "html.parser")
    a_tag = soup.select_one(".block-card_clickable:nth-of-type(3) a")

    assert a_tag["href"] == "/page-1/"


@pytest.mark.django_db
def test_card_image_block_external_url(db, django_db_setup, client: Client):
    response = client.get("/promo-hub/")
    soup = BeautifulSoup(response.content, "html.parser")
    block = soup.select(".block-card_image")[0]
    a_tag = block.find("a")

    assert a_tag["href"] == "https://example.com/"


@pytest.mark.django_db
def test_card_image_block_internal_page(db, django_db_setup, client: Client):
    response = client.get("/promo-hub/")
    soup = BeautifulSoup(response.content, "html.parser")
    block = soup.select(".block-card_image")[1]
    a_tag = block.find("a")

    assert a_tag["href"] == "/page-1/"


@pytest.mark.django_db
def test_card_image_block_no_internal_link_or_url(db, django_db_setup, client: Client):
    response = client.get("/promo-hub/")
    soup = BeautifulSoup(response.content, "html.parser")
    block = soup.select(".block-card_image")[2]
    a_tag = block.find("a")

    assert not a_tag
