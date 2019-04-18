from django import forms

class MultiChoiceBoundField(forms.BoundField):
    
    @property
    def fieldset(self):
        return self.field.fieldset

    
class Checkbox(forms.MultipleChoiceField):
    
    def __init__(self, *, label='', **kwargs):
        self.fieldset = label
        super().__init__(label='',
                         widget=forms.CheckboxSelectMultiple,
                         **kwargs)
        
    def get_bound_field(self, form, field_name):
        return MultiChoiceBoundField(form, self, field_name)
    
class Radio(forms.ChoiceField):
    
    def __init__(self, *, label='', inline=False, **kwargs):
        self.fieldset = label
        self.attrs = { 'inline': inline }
        super().__init__(label='',
                         widget=forms.RadioSelect(attrs=self.attrs),
                         **kwargs)
        
    def get_bound_field(self, form, field_name):
        return MultiChoiceBoundField(form, self, field_name)
    
class TextInput(forms.CharField):
    
    def __init__(self, *, width=None,**kwargs):
        self.attrs = { 'width': width }
        super().__init__(widget=forms.TextInput(attrs=self.attrs),
                         **kwargs)

class TextArea(forms.CharField):
    
    def __init__(self, *, rows=5, **kwargs):
        self.attrs = {'rows': rows}
        super().__init__(widget=forms.Textarea(attrs=self.attrs),
                         **kwargs)
        
class Select(forms.ChoiceField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)