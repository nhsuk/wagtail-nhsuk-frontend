from django import forms

from wagtailnhsukfrontend.forms.templatetags.nhsukfrontendforms_tags import (
    add_class,
    add_widget_classes,
    is_checkbox,
)


def test_add_class_to_empty_widget():
    """Test adding a class to widget without preexisting class attribute"""
    widget = forms.CheckboxInput(attrs={})
    new_class = "new-class"
    expected = {"attrs": {"class": "new-class"}}
    result = add_class(widget.__dict__, new_class)
    assert result["attrs"] == expected["attrs"]


def test_add_class_to_widget_with_class():
    """Test adding a class to widget with preexisting class attribute"""
    widget = forms.CheckboxInput(attrs={"class": "old-class"})
    new_class = "new-class"
    expected = {"attrs": {"class": "old-class new-class"}}
    result = add_class(widget.__dict__, new_class)
    assert result["attrs"] == expected["attrs"]


class ExampleForm(forms.Form):
    text = forms.CharField()
    checkbox = forms.BooleanField()


def test_add_widget_classes_simple():
    """Test when field has no errors and not initially hidden"""
    form = ExampleForm({"text": "some text here"})
    field = form["text"]
    result = add_widget_classes(field)
    expected = '<input type="text" name="text" value="some text here" class="nhsuk-input" required id="id_text">'
    assert result == expected


def test_add_widget_classes_error_on_field():
    """Test when field has errors"""
    form = ExampleForm({"text": ""})
    field = form["text"]
    result = add_widget_classes(field)
    expected = '<input type="text" name="text" class="nhsuk-input nhsuk-input--error" required id="id_text">'
    assert result == expected


def test_widget_is_not_checkbox():
    """Test widget is not a checkbox"""
    form = ExampleForm()
    field = form["text"]
    assert is_checkbox(field) is False


def test_widget_is_checkbox():
    """Test widget is a checkbox"""
    form = ExampleForm()
    field = form["checkbox"]
    assert is_checkbox(field) is True
