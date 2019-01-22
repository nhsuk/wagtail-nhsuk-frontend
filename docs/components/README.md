# Components

There are a few different types of component which should be used in different
ways.

### Blocks

Block-type components use wagtail blocks for use in a [streamfield](https://docs.wagtail.io/en/v2.0/topics/streamfield.html).

example: [ActionLink](./action-link.md)

### Templatetags

Templatetag-type components can be included in templates with [django templatetags](https://docs.djangoproject.com/en/2.1/howto/custom-template-tags/).

example: [Breadcrumb](./breadcrumb.md)

### Template includes

Template includes can be used with the `{% include %}` tag in your templates.

example: [Header (via templates)](./header.md#direct-use-of-templates)

### Settings

Wagtail site settings must be enabled with the `wagtailnhsstyle.settings` app.

example: [Header (via settings)](./header.md#wagtail-site-settings)

## List of Components

- [Action Link](./action_link.md)
- [Breadcrumb](./breadcrumb.md)
- [Callout](./callout.md)
- [Care Card](./care_card.md)
- [Header](./header.md)
