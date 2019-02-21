from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel


class ReviewDateMixin(models.Model):

    last_review_label = models.CharField(verbose_name="Reviewed date label", max_length=120, help_text="The default for NHS frontend is: Page last reviewed:")
    reviewed_date = models.DateTimeField(null=True, help_text="This will be displayed as Month/Year")
    next_review_label = models.CharField(blank=True, null=True, max_length=120, help_text="The default for NHS frontend is: Page last reviewed: - Leave this empty if you do not want to add Next review date")
    next_review_date = models.DateTimeField(blank=True, null=True, help_text="This will be displayed as Month/Year")

    settings_panels = [
        MultiFieldPanel(
            [
                FieldPanel('last_review_label'),
                FieldPanel('reviewed_date'),
                FieldPanel('next_review_label'),
                FieldPanel('next_review_date')
            ]
        ),
    ]

    class Meta:

        abstract = True
