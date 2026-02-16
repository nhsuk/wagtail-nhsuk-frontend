import pytest
from wagtailnhsukfrontend.blocks import TableBlock


@pytest.mark.django_db
class TestTableBlock():
    def test_table_caption_css_class(self):
        block = TableBlock()

        cleaned = block.clean({
            'caption': 'Test Caption',
        })

        html = block.render(cleaned)

        assert 'Test Caption' in html
        assert 'class="nhsuk-table__caption' in html

    def test_table_caption_size_css_class(self):
        block = TableBlock()

        cleaned = block.clean({
            'caption': 'Test Caption',
            'caption_size': 'l'
        })

        html = block.render(cleaned)

        assert 'Test Caption' in html
        assert 'nhsuk-table__caption--l' in html

    def test_table_responsive_css_class(self):
        block = TableBlock()

        cleaned = block.clean({
            'responsive': True
        })

        html = block.render(cleaned)

        assert 'nhsuk-table-responsive' in html
        assert 'role="table"' in html

    def test_table_not_responsive_css_class(self):
        block = TableBlock()

        cleaned = block.clean({
            'responsive': False
        })

        html = block.render(cleaned)

        assert 'nhsuk-table' in html
        assert 'role="table"' not in html

    def test_table_header_cells(self):
        block = TableBlock()

        cleaned = block.clean({
            'head': [
                {
                    'text': 'Header 1',
                    'format': 'numeric',
                    'classes': 'custom-class'
                },
                {
                    'text': 'Header 2'
                }
            ]
        })

        html = block.render(cleaned)

        assert 'Header 1' in html
        assert 'Header 2' in html
        assert 'nhsuk-table__header--numeric' in html
        assert 'custom-class' in html

    def test_table_colspan_rowspan(self):
        block = TableBlock()

        cleaned = block.clean({
            'head': [
                {
                    'text': 'Header with span',
                    'colspan': '2',
                    'rowspan': '3'
                }
            ]
        })

        html = block.render(cleaned)

        assert 'colspan="2"' in html
        assert 'rowspan="3"' in html

    def test_table_body_rows(self):
        block = TableBlock()

        cleaned = block.clean({
            'rows': [
                {
                    'cells': [
                        {'text': 'Cell 1'},
                        {'text': 'Cell 2', 'format': 'numeric'}
                    ]
                }
            ]
        })

        html = block.render(cleaned)

        assert 'Cell 1' in html
        assert 'Cell 2' in html
        assert 'nhsuk-table__cell--numeric' in html

    def test_table_first_cell_is_header(self):
        block = TableBlock()

        cleaned = block.clean({
            'first_cell_is_header': True,
            'rows': [
                {
                    'cells': [
                        {'text': 'Row header'},
                        {'text': 'Regular cell'}
                    ]
                }
            ]
        })

        html = block.render(cleaned)

        assert '<th scope="row" class="nhsuk-table__header' in html
        assert 'Row header\n                        </th>' in html
        assert '<td class="nhsuk-table__cell' in html
        assert 'Regular cell\n                        </td>' in html
        assert 'nhsuk-table__cell--numeric' not in html
