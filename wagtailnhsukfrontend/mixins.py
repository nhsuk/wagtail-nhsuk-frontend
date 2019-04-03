from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel


class ReviewDateMixin(models.Model):

    last_review_date = models.DateTimeField(blank=True, null=True)
    next_review_date = models.DateTimeField(blank=True, null=True)

    last_review_label = 'Page last reviewed:'
    next_review_label = 'Next review due:'

    settings_panels = [
        MultiFieldPanel(
            [
                FieldPanel('last_review_date'),
                FieldPanel('next_review_date')
            ],
            heading="Review Dates",
        ),
    ]

    class Meta:

        abstract = True
