from wagtailnhsukfrontend.templatetags.nhsukfrontend_tags import chunk

LIST = [1, 2, 3, 4, 5, 6, 7]


def test_chunk_tag_size_2():
    result = chunk(LIST, 2)
    expected = [[1, 2], [3, 4], [5, 6], [7]]
    assert result == expected


def test_chunk_tag_size_8():
    result = chunk(LIST, 8)
    expected = [[1, 2, 3, 4, 5, 6, 7]]
    assert result == expected
