from django import template

register = template.Library()


@register.tag(name="contentwrapper")
def content_wrapper(parser, token):
    """
    Add wrapper element.
    It doesn't do anything here in this context.
    It will be overridden by another app if necessary
    """
    try:
        tag_name, variable_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires variable as parameter" % token.contents.split()[0]
        )
    nodelist = parser.parse(("endcontentwrapper",))
    parser.delete_first_token()
    return ContentWrapperNode(nodelist, variable_name)


class ContentWrapperNode(template.Node):
    def __init__(self, nodelist, variable_name):
        self.nodelist = nodelist
        self.variable_name = variable_name

    def render(self, context):
        output = self.nodelist.render(context)
        return output
