

# Feedback banner

To add the **default** feedback banner just paste this in your `home_page.html` template.
```django
{% include 'wagtailnhsukfrontend/feedback_banner.html' %}
```

| Option | Description |
| ------ | ----------- |
| `title` | Title to display for the for the banner
| `content` |  Content of the feedback banner component
| `label` |  Optional text to be displayed within the link at the end of the content
| `url` |  Optional value of the link href attribute at the end of the content

This example makes use of all the options that can be passed.
```django
    {% include 'wagtailnhsukfrontend/feedback_banner.html' with  title="Test" content="This is test content" url="http://example.com/" label="Example URL label"%}
```

## Reference

[Service Manual](https://beta.nhs.uk/service-manual/styles-components-patterns/feedback-banner)  
[Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/feedback-banner)

