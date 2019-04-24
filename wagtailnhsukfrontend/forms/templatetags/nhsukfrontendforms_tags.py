from django import template

register = template.Library()

@register.filter
def add_class(widget, new_class):
    attrs = widget['attrs']

    if 'class' in attrs:
        attrs['class'] = attrs['class'] + ' {0}'.format(new_class)
    else:
        attrs['class'] = new_class

    widget['attrs'] = attrs
    return widget


@register.inclusion_tag('forms/form_as_div.html')
def nhsuk_form(form):
    return {'form': form}
