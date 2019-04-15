# Components

There are a few different types of component which should be used in different
ways.

### Blocks

Block-type components use wagtail blocks for use in a [streamfield](https://docs.wagtail.io/en/v2.0/topics/streamfield.html).

example: [ActionLink](./action_link.md)

### Templatetags

Templatetag-type components can be included in templates with [django templatetags](https://docs.djangoproject.com/en/2.1/howto/custom-template-tags/).

example: [Breadcrumb](./breadcrumb.md)

### Template includes

Template includes can be used with the `{% include %}` tag in your templates.

example: [Header (via templates)](./header.md#direct-use-of-templates)

### Settings

Wagtail site settings must be enabled with the `wagtailnhsukfrontend.settings` app.

example: [Header (via settings)](./header.md#wagtail-site-settings)

## List of Components

- [Action Link](./action_link.md)
- [Back Link](./back_link.md)
- [Breadcrumb](./breadcrumb.md)
- [Care Card](./care_card.md)
- [Details](./details.md)
- [Do List](./do.md)
- [Don't List](./dont.md)
- [Emergency Alert](./emergency_alert.md)
- [Expander & Expander Group](./expander.md)
- [Favicons](./favicons.md)
- [Feedback banner](./feedback_banner.md)
- [Header](./header.md)
- [Inset Text](./inset_text.md)
- [Image](./image.md)
- [Panel](./panel.md)
- [Promo & and Promo Group](./promo.md)
- [Skip Link](./skip_link.md)
- [Warning Callout](./warning_callout.md)
- [Review Date](./review_date.md)
