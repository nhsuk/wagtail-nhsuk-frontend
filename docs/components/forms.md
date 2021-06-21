# Forms

Before implementing any forms, make sure you have read the guidance in the Digital Service Manual [https://service-manual.nhs.uk/content/how-to-write-good-questions-for-forms](https://service-manual.nhs.uk/content/how-to-write-good-questions-for-forms).

## Settings

Add the `wagtailnhsukfrontend.forms` app to `INSTALLED_APPS`.

```py
INSTALLED_APPS = [
    ...
    'wagtailnhsukfrontend.forms',
    ...
]
```

Add the `FORM_RENDERER` setting to tell django to use the nhsukfrontend form templates.

```py
FORM_RENDERER = 'wagtailnhsukfrontend.forms.renderers.NHSUKFrontendRenderer'
```

## Rendering the form

Form fields can be rendered with the `nhsuk_form` templatetag.  
As usual with Django forms, it is your responsibility to render the `<form>` element, submit button and csrf_token as appropriate.

Assuming you have a `form` in your template context which is a `django.forms.Form` instance;
```django
{% load nhsukfrontendforms_tags %}

<form method="POST" novalidate>
  {% csrf_token %}

  {% nhsuk_form form %}

  <input class="nhsuk-button" type="submit" value="Submit" />
</form>
```
