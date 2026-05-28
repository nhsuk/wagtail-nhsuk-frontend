# Inset Text

```py
from wagtail.models import Page
from wagtail.fields import StreamField

from wagtailnhsukfrontend.blocks import TaskListBlock

class MyPage(Page):
  body = StreamField([
      ...
      ('task_list', TaskListBlock()),
      ...
  ], use_json_field=True)
```

## Reference

* [Service Manual](https://service-manual.nhs.uk/design-system/components/task-list)
