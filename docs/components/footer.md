# Footer

## Wagtail Site Settings

wagtail-nhs-style comes with a wagtail
[site settings](http://docs.wagtail.io/en/v2.4/reference/contrib/settings.html)
model. If you want to allow CMS users to configure the footer in the wagtail
interface, use of the site setting is recommended.

Add the `wagtailnhsukfrontend.settings` module to your `INSTALLED_APPS` config.

```python
INSTALLED_APPS = [
  ...
  'wagtailnhsukfrontend',
  'wagtailnhsukfrontend.settings',
  ...
]
```

This will create a new option under `Settings > Footer settings` in the
wagtail interface.

To include the footer in your template, use the `header` templatetag.

```python
{% load nhsukfrontendsettings_tags %}

...

<body>
  ...
  {% footer %}
</body>
```
---

The NHS.UK footer component can be configured in two styles:

---

## Column-based Footer

The column-based footer allows content to be organised into up to 4 columns. Each column can contain multiple links to either internal Wagtail pages or external URLs.

### Enabling Column-based Footer

1. In Wagtail Admin, navigate to **Settings > Footer Column Settings**
2. Tick **"Enable column-based footer"**
3. Add footer links using the **"Footer Column Links"** panel
4. For each link:
   - Select the column number (1–4)
   - Enter the link label
   - Choose either:
     - An internal page using **"Link page"**
     - An external URL using **"Link URL"**

### Template Usage

```django
{% include 'wagtailnhsukfrontend/footer.html' %}
```

The template automatically detects which footer style to use based on your settings.

## Standard Footer
The standard footer provides a single column of links and can be configured through Settings > Footer Settings.

### Configuration
1. In Wagtail Admin, navigate to Settings > Footer Settings
2. Add footer links using the "Footer Links" panel
3. For each link:
 - Enter the URL
 - Enter the link label

### Template Usage
```django
{% include 'wagtailnhsukfrontend/footer.html' %}
```

### Customisation
Both footer styles include:

- NHS copyright notice
- Semantic HTML with proper ARIA roles
- Responsive design following NHS.UK frontend standards


## Reference

* [Service Manual](https://service-manual.nhs.uk/design-system/components/footer)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/footer)
