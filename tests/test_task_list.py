import pytest
from wagtail.models import Page
from wagtailnhsukfrontend.blocks import TaskListBlock


@pytest.mark.django_db
class TestTaskListBlock():
    def test_task_list_external_url(self):
        block = TaskListBlock()

        cleaned = block.clean({
            'tasks': [
                {
                    'title': 'Test Title',
                    'external_url': 'https://testurl.com',
                    'hint': '',
                    'status': [
                        ('text', {'status_text': 'Completed', 'cannot_start_yet': False})
                    ]
                }
            ]
        })

        html = block.render(cleaned)

        assert 'href="https://testurl.com"' in html
        assert 'Test Title' in html
        assert 'aria-describedby="test-title-status"' in html
        assert 'id="test-title-status"' in html

    def test_task_list_internal_link(self):
        home = Page.objects.get(id=1)
        internal_page = home.add_child(
            instance=Page(title='Test page', slug='test-page')
        )

        block = TaskListBlock()

        cleaned = block.clean({
            'tasks': [
                {
                    'title': 'Test Title',
                    'internal_page': internal_page,
                    'hint': '',
                    'status': [
                        ('text', {'status_text': 'Completed', 'cannot_start_yet': False})
                    ]
                }
            ]
        })

        html = block.render(cleaned)

        assert f'href="{internal_page.url}"' in html
        assert 'Test Title' in html
        assert 'aria-describedby="test-title-status"' in html
        assert 'id="test-title-status"' in html

    def test_task_list_completed_css_class(self):
        block = TaskListBlock()

        cleaned = block.clean({
            'tasks': [
                {
                    'title': 'Test Title',
                    'status': [
                        ('text', {'status_text': 'Completed', 'cannot_start_yet': False})
                    ]
                }
            ]
        })

        html = block.render(cleaned)

        assert 'nhsuk-task-list__status--completed' in html
        assert 'Completed' in html

    def test_task_list_not_started_css_class(self):
        block = TaskListBlock()

        cleaned = block.clean({
            'tasks': [
                {
                    'title': 'Test Title',
                    'status': [
                        ('text', {'status_text': 'Not started', 'cannot_start_yet': True})
                    ]
                }
            ]
        })

        html = block.render(cleaned)

        assert 'nhsuk-task-list__status--cannot-start-yet' in html
        assert 'Not started' in html
