
# Skip Link

```django
{% include 'wagtailnhsukfrontend/skip_link.html' %}
```
| Option | Description | Default |
| ------ | ----------- | ------- |
| `text` | Title to display for the link | `Skip to main content` |
| `href` |  The href tag for the skip link| `#maincontent` |

To ensure that the skip link works as intended make sure its the first include in the template. You can also pass the two options above using `with`  after the `include` tag.


```django
{% include 'wagtailnhsukfrontend/skip_link.html' with  href="#demo" text="Demo Text"%}
```
## Reference

* [Service Manual](https://service-manual.nhs.uk/design-system/components/skip-link)
* [Frontend Library](https://github.com/nhsuk/nhsuk-frontend/tree/master/packages/components/skip-link)

