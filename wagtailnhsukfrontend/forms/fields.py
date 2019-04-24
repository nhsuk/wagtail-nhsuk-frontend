from django import forms

class MultiChoiceBoundField(forms.BoundField):
    
    @property
    def fieldset(self):
        return self.field.fieldset

    
class Checkbox(forms.MultipleChoiceField):
    error_class = None
    
    def __init__(self, label='', name=None, help_text='', **kwargs):
        self.fieldset = label
        self.attrs = {}
        self._set_classes()
        self._set_aria(name, help_text)
        super().__init__(label='',
                         widget=forms.CheckboxSelectMultiple(attrs=self.attrs),
                         help_text=help_text, **kwargs)
        
    def get_bound_field(self, form, field_name):
        return MultiChoiceBoundField(form, self, field_name)
    
    def _set_classes(self):
        self.attrs['class'] = 'nhsuk-checkboxes'
        
    def _set_aria(self, name, help_text):
        if help_text:
            self.attrs['aria-describedby'] = '{}-hint'.format(name)
    
class Radio(forms.ChoiceField):
    error_class = None

    def __init__(self, label='', inline=False, name=None, help_text='', **kwargs):
        self.fieldset = label
        self.attrs = {}
        self._set_classes(inline)
        self._set_aria(name, help_text)
        super().__init__(label='',
                         widget=forms.RadioSelect(attrs=self.attrs),
                         help_text=help_text, **kwargs)
        
    def get_bound_field(self, form, field_name):
        return MultiChoiceBoundField(form, self, field_name)
    
    def _set_classes(self, inline):
        self.attrs['class'] = 'nhsuk-radios'
        
        if inline:
            self.attrs['class'] += ' nhsuk-radios--inline'
        
    def _set_aria(self, name, help_text):
        if help_text:
            self.attrs['aria-describedby'] = '{}-hint'.format(name)
    
class TextInput(forms.CharField):
    error_class = 'nhsuk-input--error'
    
    def __init__(self, width=None, name=None, help_text='', **kwargs):
        self.attrs = {}
        self._set_classes(width)
        self._set_aria(name, help_text)
        super().__init__(widget=forms.TextInput(attrs=self.attrs),
                         **kwargs)
        
    def _set_classes(self, width):
        self.attrs['class'] = 'nhsuk-input'
        
        if width:
            self.attrs['class'] += ' nhsuk-input--width-{}'.format(width)
            
    def _set_aria(self, name, help_text):
        if help_text:
            self.attrs['aria-describedby'] = '{}-hint'.format(name)
        

class TextArea(forms.CharField):
    error_class = 'nhsuk-textarea--error'
    
    def __init__(self, rows=5, name=None, help_text='', **kwargs):
        self.attrs = {}
        self._set_classes(rows)
        self._set_aria(name, help_text)
        super().__init__(widget=forms.Textarea(attrs=self.attrs),
                         help_text=help_text, **kwargs)
        
    def _set_classes(self, rows):
        self.attrs['class'] = 'nhsuk-textarea'
        self.attrs['rows'] = rows
        
    def _set_aria(self, name, help_text):
        if help_text:
            self.attrs['aria-describedby'] = '{}-hint'.format(name)
        
class Select(forms.ChoiceField):
    error_class = 'nhsuk-select--error'
    
    def __init__(self, name=None, help_text='', **kwargs):
        self.attrs = {}
        self._set_classes()
        self._set_aria(name, help_text)
        super().__init__(widget=forms.Select(attrs=self.attrs),
                         help_text=help_text, **kwargs)
        
    def _set_classes(self):
        self.attrs['class'] = 'nhsuk-select'
        
    def _set_aria(self, name, help_text):
        if help_text:
            self.attrs['aria-describedby'] = '{}-hint'.format(name)
            