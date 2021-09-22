from django import template

register = template.Library()


@register.simple_tag
def add_extra_parameters(variable_name):
    """
    Add extra paramaters.
    It doesn't do anything here in this context.
    It will be overridden by another app if necessary
    """
    return ""
