# Emergency Alert

```django
{% include "wagtailnhsukfrontend/emergency_alert" with title="National flu outbreak" content="There has been a national flu outbreak." %}
```

## Template Parameters

| name | description |
| ---- | ----------- |
| title | Title of the emergency alert |
| content | Main text describing the alert |
| label | Label of a call-to-action link |
| href | href of the call-to-action link |
| last_updated_string | "Updated at" text as a string |
| last_updated | "Updated at" datetime |

### Label and href

`label` and `href` must both be defined in order for the call-to-action link to
be rendered.

### Last Updated

If `last_updated_string` is passed to the template, it will be used as the label
showing when the alert was last updated.
Otherwise, `last_updated` can be passed as a datetime object which will be rendered
as a human-readable update time.
