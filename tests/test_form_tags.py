import re

from django import forms

from wagtailnhsukfrontend.forms.templatetags.nhsukfrontendforms_tags import (
    add_class,
    add_widget_classes,
    is_checkbox,
)


def get_classes_from_html_attr(html_string):
    """Extracts CSS classes from the class attribute of an HTML string."""
    match = re.search(r'class="([^"]*)"', html_string)
    if match:
        return set(match.group(1).split())
    return set()


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

    # Check for essential tag structure and attributes
    assert "<input" in result
    assert 'type="text"' in result
    assert 'name="text"' in result
    assert 'value="some text here"' in result
    assert 'id="id_text"' in result
    assert "required" in result

    # Check for classes
    classes = get_classes_from_html_attr(result)
    assert "nhsuk-input" in classes
    assert "nhsuk-input--error" not in classes


def test_add_widget_classes_error_on_field():
    """Test when field has errors"""
    form = ExampleForm({"text": ""})
    field = form["text"]
    result = add_widget_classes(field)

    # Check for essential tag structure and attributes
    assert "<input" in result
    assert 'type="text"' in result
    assert 'name="text"' in result
    assert 'id="id_text"' in result
    assert "required" in result

    # Check for classes
    classes = get_classes_from_html_attr(result)
    assert "nhsuk-input" in classes
    assert "nhsuk-input--error" in classes
    # ARIA attributes (aria-invalid, aria-describedby) are no longer checked
    # to make the test Django version-agnostic.


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
