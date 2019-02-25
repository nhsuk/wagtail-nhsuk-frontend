
# Back Link

The back link component can be included through the template only. It won't appear in the Wagtail admin interface.

Paste this on the page you want to include the back link in:
```django
{% include 'wagtailnhsukfrontend/back_link.html' %}
```

There are some options that have to be pased to the back link to make it functional:

| Option | Description | Default |
| ------ | ----------- | ------- |
| `link_title` | Title to display for the link | `None` |
| `back_url` | Set to to the URL you want the user to click on to go to the previous page | `None` |

# Reference

[Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/back-link) . 
[Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/back-link)
