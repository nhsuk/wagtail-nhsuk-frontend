import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


class FormStreamfieldBlockTests(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)
        self.driver.get('http://localhost:8080/form-page/')

    def tearDown(self):
        self.driver.close()

    def test_label_map(self):
        """
        tests label is clickable and moves focus to the correct element
        """
        fields = ['input-normal', 'input-width-2',
                  'input-width-3', 'input-width-4', 'input-width-5',
                  'input-width-10', 'input-width-20',
                  'select', 'textarea']

        for field in fields:
            element = self.driver.find_element_by_name(field)
            self._click_label(field)
            error_msg = 'Form item with id: id_{} has incorrect label mapping'.format(field)
            self.assertTrue(element == self.driver.switch_to.active_element, error_msg)

    def test_label_map_disabled(self):
        """
        test label for disabled elements, checkbox and radio
        """
        fields = ['input-disabled', 'select-disabled', 'textarea-disabled',
                  'checkbox-disabled', 'radio-disabled']

        for field in fields:
            element = self.driver.find_element_by_name(field)
            self._click_label(field)
            error_msg = 'Form item with id: id_{} has incorrect label mapping'.format(field)
            self.assertFalse(element == self.driver.switch_to.active_element, error_msg)

    def test_hint_text(self):
        hint_map = {
            'input-normal': 'input hint',
            'select': 'select hint',
            'textarea': 'textarea hint',
            'checkbox': 'checkbox hint',
            'radio': 'radio hint'
        }

        for field in hint_map:
            hint_text = hint_map.get(field)
            self._assert_hint_text(field, hint_text)

    def test_input_missing_field_error_msg(self):
        fields = ['input-normal', 'input-width-2', 'input-disabled',
                  'input-width-3', 'input-width-4', 'input-width-5',
                  'input-width-10', 'input-width-20']

        self._submit_form()

        for field in fields:
            if field == 'input-normal':
                error_text = 'custom missing field error input'
            else:
                error_text = 'This field is required'
            self._assert_error_text(field, error_text)

    def test_input_validation_error_msg(self):
        input = self._get_form_item('input-normal')
        input.send_keys('hello world')
        self._submit_form()

        self._assert_error_text('input-normal', 'custom validation error input')

    def test_input_validation(self):
        fields = ['input-normal', 'input-width-2',
                  'input-width-3', 'input-width-4', 'input-width-5',
                  'input-width-10', 'input-width-20']

        for field in fields:
            input = self._get_form_item(field)
            input.send_keys('test')
            self._submit_form()
            self._assert_no_error_text(field)

    def test_select_missing_field_error_msg(self):
        self._submit_form()
        self._assert_error_text('select-disabled', 'This field is required')

    def test_select_validation_error_msg(self):
        self._submit_form()
        self._assert_error_text('select', 'custom validation error select')

    def test_select_validation(self):
        select = Select(self._get_form_item('select'))
        select.select_by_visible_text('select 2')
        self._submit_form()
        self._assert_no_error_text('select')

    def test_textarea_missing_field_error_msg(self):
        fields = ['textarea', 'textarea-disabled']

        self._submit_form()

        for field in fields:
            if field == 'textarea':
                error_text = 'custom missing field error ta'
            else:
                error_text = 'This field is required'

            self._assert_error_text(field, error_text)

    def test_textarea_validation_error_msg(self):
        textarea = self._get_form_item('textarea')
        textarea.send_keys('test 123')
        self._submit_form()
        self._assert_error_text('textarea', 'custom validation error ta')

    def test_textarea_validation(self):
        textarea = self._get_form_item('textarea')
        textarea.send_keys('test')
        self._submit_form()
        self._assert_no_error_text('textarea')

    def test_checkbox_missing_field_error_msg(self):
        fields = ['checkbox', 'checkbox-disabled']

        self._submit_form()

        for field in fields:
            if field == 'checkbox':
                error_text = 'custom missing field error checkbox'
            else:
                error_text = 'This field is required'
            self._assert_error_text(field, error_text)

    def test_checkbox_validation_error_msg(self):
        self._click_checkbox_radio_label('Paris')
        self._submit_form()
        self._assert_error_text('checkbox', 'custom validation error checkbox')

    def test_checkbox_validation(self):
        self._click_checkbox_radio_label('London')
        self._submit_form()
        self._assert_no_error_text('checkbox')

    def test_radio_missing_field_error_msg(self):
        fields = ['radio', 'radio-disabled']

        self._submit_form()

        for field in fields:
            if field == 'radio':
                error_text = 'custom missing field error radio'
            else:
                error_text = 'This field is required'

            self._assert_error_text(field, error_text)

    def test_radio_validation_error_msg(self):
        self._click_checkbox_radio_label('No')
        self._submit_form()
        self._assert_error_text('radio', 'custom validation error radio')

    def test_radio_validation(self):
        self._click_checkbox_radio_label('Yes')
        self._submit_form()
        self._assert_no_error_text('radio')

    def _submit_form(self):
        submit_button = self.driver.find_element_by_id('form-submit-button')
        submit_button.click()

    def _assert_error_text(self, id, error_text):
        error = self.driver.find_element_by_id('{}-error'.format(id))
        self.assertEqual(error_text, error.text)

    def _assert_hint_text(self, id, hint_text):
        hint = self.driver.find_element_by_id('{}-hint'.format(id))
        self.assertEqual(hint_text, hint.text)

    def _click_label(self, id):
        label = self.driver.find_element_by_id('{}-label'.format(id))
        label.click()

    def _assert_no_error_text(self, id):
        errors = self.driver.find_elements_by_id('{}-error'.format(id))
        self.assertFalse(errors)

    def _get_form_item(self, id):
        return self.driver.find_element_by_id('id_{}'.format(id))

    def _click_checkbox_radio_label(self, label_text):
        labels = self.driver.find_elements_by_tag_name('label')
        for label in labels:
            if label.text == label_text:
                label.click()
                break


if __name__ == '__main__':
    unittest.main(warnings='ignore')
