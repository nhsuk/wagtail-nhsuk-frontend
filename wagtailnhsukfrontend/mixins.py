from django.db import models
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from django.core.exceptions import ValidationError


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


class HeroMixin(models.Model):
    """
    A Mixin to add the model for Hero components.

    """

    hero_text = models.TextField(blank=True, default='')
    hero_heading = models.TextField(default='')
    hero_image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = [MultiFieldPanel([FieldPanel('hero_heading'), FieldPanel('hero_text'), ImageChooserPanel('hero_image')], heading="Hero content")]

    def clean(self):
        if not (self.hero_text or self.hero_image):
            raise ValidationError("Hero text or image must be selected")
        else:
            pass

    class Meta:
        abstract = True
