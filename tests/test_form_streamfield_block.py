import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class FormStreamfieldBlockTests(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:9515',
            desired_capabilities=DesiredCapabilities.CHROME)
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
            
        
    def test_input_field_text(self):       
        fields = ['input-normal', 'input-width-2', 'input-disabled',
                  'input-width-3', 'input-width-4', 'input-width-5',
                  'input-width-10', 'input-width-20']
        
        for field in fields:
            input_id = 'id_{}'.format(field)
            
        
    
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
