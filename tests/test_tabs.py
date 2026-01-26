from wagtailnhsukfrontend.blocks import TabsBlock


class TestTabBlock():
    def test_tab_link_id(self):
        block = TabsBlock()

        cleaned = block.clean({
            'tabs': [
                {
                    'label': 'Tab One Label',
                    'body': [
                        {'type': 'richtext', 'value': 'Tab one content'}
                    ]
                },
                {
                    'label': 'Tab Two Label',
                    'body': [
                        {'type': 'richtext', 'value': 'Tab two content'}
                    ]
                }
            ]
        })

        html = block.render(cleaned)

        assert 'href="#tab-one-label"' in html
        assert 'id="tab-one-label"' in html
        assert 'href="#tab-two-label"' in html
        assert 'id="tab-two-label"' in html
