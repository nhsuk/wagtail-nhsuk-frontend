# Emergency Alert

## Settings

If you have the `wagtailnhsukfrontend.settings` module installed, you will see
an option under `Settings > Emergency Alert` in the wagtail admin menu.

To include the emergency alert in your template, use the templatetag in your base template.
```django
{% load nhsukfrontendsettings_tags %}

<!-- above your header -->
{% emergency_alert %}
```

## Direct use of the template

```django
{% include "wagtailnhsukfrontend/emergency_alert" with title="National flu outbreak" content="There has been a national flu outbreak." %}
```

### Template parameters

| Option | Description |
| ------ | ----------- |
| title | Title of the emergency alert |
| content | Main text describing the alert |
| label | Label of a call-to-action link |
| href | href of the call-to-action link |
| last_updated_string | "Updated at" text as a string |
| last_updated | datetime object to use when rendering the "Updated at" label |

### Label and href

`label` and `href` must both be defined in order for the call-to-action link to
be rendered.

### Last Updated

If `last_updated_string` is passed to the template, it will be used as the label
showing when the alert was last updated.
Otherwise, `last_updated` can be passed as a datetime object which will be rendered
as a human-readable update time.

## Reference

[Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/emergency-alert)
