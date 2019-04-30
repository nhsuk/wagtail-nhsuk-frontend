from django import forms
from wagtailnhsukfrontend.forms.fields import TextInput, Select, TextArea, \
    Checkbox, Radio
import re
from django.core.exceptions import ValidationError
from django.forms.fields import FileField


class FieldSelector(object):

    def get_field(self, field, name):
        type = field['type']
        attrs = field.get('value', {})
        label = attrs.get('label', '')
        hint = attrs.get('hint', '')
        required = attrs.get('required', True)
        disabled = attrs.get('disabled', False)
        validator_regex = re.compile(attrs.get('validator', '.*'))
        validation_error_message = attrs.get('validation_error_message',
                                             'Validation error')
        error_messages = {
            'required': attrs.get('missing_field_error_message',
                                  'This field is required')
        }

        def regex_validator(value):
            if not validator_regex.match(value):
                raise forms.ValidationError(validation_error_message)

        def regex_validator_multi(values):
            for value in values:
                if not validator_regex.match(value):
                    raise forms.ValidationError(validation_error_message)

        if type == 'text_input':
            width = attrs.get('width')
            return TextInput(label=label,
                             help_text=hint,
                             required=required,
                             width=width,
                             disabled=disabled,
                             error_messages=error_messages,
                             validators=[regex_validator],
                             name=name)

        elif type == 'select':
            choices = self._get_choices(attrs)
            return Select(label=label,
                          help_text=hint,
                          required=required,
                          choices=choices,
                          disabled=disabled,
                          error_messages=error_messages,
                          validators=[regex_validator],
                          name=name)

        elif type == 'textarea':
            rows = attrs.get('rows')
            return TextArea(label=label,
                            help_text=hint,
                            required=required,
                            rows=rows,
                            disabled=disabled,
                            error_messages=error_messages,
                            validators=[regex_validator],
                            name=name)

        elif type == 'checkbox':
            choices = self._get_choices(attrs)
            return Checkbox(label=label,
                            help_text=hint,
                            required=required,
                            choices=choices,
                            disabled=disabled,
                            error_messages=error_messages,
                            validators=[regex_validator_multi],
                            name=name)

        elif type == 'radio':
            choices = self._get_choice_groups(attrs)
            inline = attrs.get('inline', False)
            return Radio(label=label,
                         help_text=hint,
                         required=required,
                         choices=choices,
                         disabled=disabled,
                         inline=inline,
                         error_messages=error_messages,
                         validators=[regex_validator],
                         name=name)

    @staticmethod
    def _get_choices(attrs):
        choices = []
        for choice in attrs.get('choices', []):
            choices.append((choice.get('value'), choice.get('name')))
        return choices

    @staticmethod
    def _get_choice_groups(attrs):
        choices = []
        for choice_group in attrs.get('choices'):
            group = []
            for choice in choice_group.get('value'):
                group.append((choice.get('value'), choice.get('name')))
            choices.append(('group', group))
        return choices


class FormCreator(forms.Form):

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('form_fields')
        self.field_selector = FieldSelector()
        super(FormCreator, self).__init__(*args, **kwargs)

        for i, field in enumerate(fields):
            field_name = field.get('value', {}).get('name', None)
            if not field_name:
                field_name = 'form_field_{}'.format(i)
            self.fields[field_name] = self.field_selector.get_field(field, field_name)

    def _clean_fields(self):
        for name, field in self.fields.items():
            # value_from_datadict() gets the data from the data dictionaries.
            # Each widget type knows how to retrieve its own data, because some
            # widgets split data over several HTML fields.
            if field.disabled:
                value = self.get_initial_for_field(field, name)
            else:
                value = field.widget.value_from_datadict(self.data, self.files, self.add_prefix(name))
            try:
                if isinstance(field, FileField):
                    initial = self.get_initial_for_field(field, name)
                    value = field.clean(value, initial)
                else:
                    value = field.clean(value)
                self.cleaned_data[name] = value
                if hasattr(self, 'clean_%s' % name):
                    value = getattr(self, 'clean_%s' % name)()
                    self.cleaned_data[name] = value
            except ValidationError as e:
                self._add_error_class(field, name)
                self.add_error(name, e)

    def _add_error_class(self, field, name):
        if field.error_class:
            field.widget.attrs['class'] += ' {}'.format(field.error_class)

        if field.widget.attrs.get('aria-describedby', None):
            field.widget.attrs['aria-describedby'] += ' {}-error'.format(name)
        else:
            field.widget.attrs['aria-describedby'] = '{}-error'.format(name)
