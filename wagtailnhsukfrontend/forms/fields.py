from django import forms

class MultiChoiceBoundField(forms.BoundField):
    
    @property
    def fieldset(self):
        return self.field.fieldset

    
class Checkbox(forms.MultipleChoiceField):
    error_class = None
    
    def __init__(self, *, label='', **kwargs):
        self.fieldset = label
        self.attrs = { 'class': 'nhsuk-checkboxes' }
        super().__init__(label='',
                         widget=forms.CheckboxSelectMultiple(attrs=self.attrs),
                         **kwargs)
        
    def get_bound_field(self, form, field_name):
        return MultiChoiceBoundField(form, self, field_name)
    
class Radio(forms.ChoiceField):
    error_class = None

    def __init__(self, *, label='', inline=False, **kwargs):
        self.fieldset = label
        self.attrs = { 'class': 'nhsuk-radios' }
        self._get_attrs(inline)
        super().__init__(label='',
                         widget=forms.RadioSelect(attrs=self.attrs),
                         **kwargs)
        
    def get_bound_field(self, form, field_name):
        return MultiChoiceBoundField(form, self, field_name)
    
    def _get_attrs(self, inline):
        if inline:
            self.attrs['class'] += ' nhsuk-radios--inline'
    
class TextInput(forms.CharField):
    error_class = 'nhsuk-input--error'
    
    def __init__(self, *, width=None,**kwargs):
        self.attrs = { 'class': 'nhsuk-input' }
        self._get_attrs(width)
            
        super().__init__(widget=forms.TextInput(attrs=self.attrs),
                         **kwargs)
        
    def _get_attrs(self, width):
        if width:
            self.attrs['class'] += ' nhsuk-input--width-{}'.format(width)

class TextArea(forms.CharField):
    error_class = 'nhsuk-textarea--error'
    
    def __init__(self, *, rows=5, **kwargs):
        self.attrs = {'rows': rows,
                      'class': 'nhsuk-textarea'}
        super().__init__(widget=forms.Textarea(attrs=self.attrs),
                         **kwargs)
        
class Select(forms.ChoiceField):
    error_class = 'nhsuk-select--error'
    
    def __init__(self, **kwargs):
        self.attrs = { 'class': 'nhsuk-select' }
        super().__init__(widget=forms.Select(attrs=self.attrs), **kwargs)
        