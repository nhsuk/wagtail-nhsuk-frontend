from wagtail.core.blocks import (
    StreamBlock,
    StructBlock,
    CharBlock,
    ChoiceBlock,
    ListBlock,
    IntegerBlock,
    BooleanBlock
)

class FormFieldChoiceBlock(StructBlock):
    name = CharBlock(required=True)
    value = CharBlock(required=True)
    
class FormFieldChoiceGroupBlock(StreamBlock):
    choice_groups = ListBlock(FormFieldChoiceBlock())
    
class BaseFormFieldBlock(StructBlock):
    label = CharBlock(required=True)
    hint = CharBlock(required=False)
    required = BooleanBlock(required=False, default=True)
    disabled = BooleanBlock(required=False, default=False)
    validator = CharBlock(required=False)
    missing_field_error_message = CharBlock(required=False, default='This field is required')
    validation_error_message = CharBlock(required=False, default='Validation error')

class InputBlock(BaseFormFieldBlock):
    width = ChoiceBlock([
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('10', '10'),
        ('20', '20')
    ],
        required=False,
        default=None)
    
    class Meta:
        icon = 'italic'
    
    
class SelectBlock(BaseFormFieldBlock):
    choices = ListBlock(FormFieldChoiceBlock, required=True)
    
    class Meta:
        icon = 'list-ul'
    
class TextareaBlock(BaseFormFieldBlock):
    rows = IntegerBlock(required=False,
                        min_value=1,
                        default=5)
    
    class Meta:
        icon = 'doc-full'
    
class CheckboxBlock(BaseFormFieldBlock):
    choices = ListBlock(FormFieldChoiceBlock, required=True)
    
    class Meta:
        icon = 'tick'
    
class RadioBlock(BaseFormFieldBlock):
    choices = FormFieldChoiceGroupBlock()
    inline = BooleanBlock(required=False)
    
    class Meta:
        icon = 'radio-empty'
           
class FormFieldBlock(StreamBlock):
    text_input = InputBlock()
    select = SelectBlock()
    textarea = TextareaBlock()
    checkbox = CheckboxBlock()
    radio = RadioBlock()