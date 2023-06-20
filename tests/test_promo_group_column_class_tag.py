import pytest

from wagtailnhsukfrontend.templatetags.nhsukfrontend_tags import (
    promo_group_column_class,
)


def test_column_size_0():
    with pytest.raises(Exception) as excinfo:
        promo_group_column_class(0)

    assert "promo column sizes must be either 2 or 3" == str(excinfo.value)


def test_column_size_2():
    result = promo_group_column_class(2)
    expected = "nhsuk-grid-column-one-half"
    assert result == expected


def test_column_size_3():
    result = promo_group_column_class(3)
    expected = "nhsuk-grid-column-one-third"
    assert result == expected
