from wagtail.contrib.settings.models import register_setting
from wagtailnhsstyle.models import HeaderSettings

@register_setting
class X(HeaderSettings):
    pass
