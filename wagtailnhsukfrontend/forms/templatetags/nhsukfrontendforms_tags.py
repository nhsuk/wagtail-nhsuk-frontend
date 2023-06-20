from django import template
from django.forms.widgets import (
    CheckboxInput,
    CheckboxSelectMultiple,
    EmailInput,
    NumberInput,
    PasswordInput,
    RadioSelect,
    Select,
    Textarea,
    TextInput,
    URLInput,
)

register = template.Library()


@register.inclusion_tag("forms/form_as_div.html")
def nhsuk_form(form):
    return {"form": form}


def _add_class(attrs, new_class):
    if "class" in attrs:
        attrs["class"] = attrs["class"] + " " + new_class
    else:
        attrs["class"] = new_class
    return attrs


@register.filter
def add_class(widget, new_class):
    attrs = widget["attrs"]
    attrs = _add_class(attrs, new_class)
    widget["attrs"] = attrs

    return widget


def get_widget_html_class(widget):
    if (
        isinstance(widget, TextInput)
        or isinstance(widget, NumberInput)
        or isinstance(widget, EmailInput)
        or isinstance(widget, URLInput)
        or isinstance(widget, PasswordInput)
    ):
        return "nhsuk-input"
    elif isinstance(widget, Textarea):
        return "nhsuk-textarea"
    elif isinstance(widget, RadioSelect):
        return "nhsuk-radios"
    elif isinstance(widget, CheckboxSelectMultiple):
        return "nhsuk-checkboxes"
    elif isinstance(widget, CheckboxInput):
        return "nhsuk-checkboxes__input"
    elif isinstance(widget, Select):
        return "nhsuk-select"
    else:
        return ""


def get_widget_html_error_class(widget):
    if (
        isinstance(widget, TextInput)
        or isinstance(widget, NumberInput)
        or isinstance(widget, EmailInput)
        or isinstance(widget, URLInput)
        or isinstance(widget, PasswordInput)
    ):
        return "nhsuk-input--error"
    elif isinstance(widget, Textarea):
        return "nhsuk-textarea--error"
    else:
        return ""


@register.filter
def add_widget_classes(field):
    widget = field.field.widget
    attrs = {}

    widget_html_class = get_widget_html_class(widget)
    attrs = _add_class(attrs, widget_html_class)

    if field.errors:
        widget_html_error_class = get_widget_html_error_class(widget)
        attrs = _add_class(attrs, widget_html_error_class)

    if field.field.show_hidden_initial:
        return field.as_widget(attrs=attrs) + field.as_hidden(
            attrs=attrs, only_initial=True
        )
    return field.as_widget(attrs=attrs)


@register.filter
def is_checkbox(field):
    return isinstance(field.field.widget, CheckboxInput)
