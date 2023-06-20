import os

import django
from django.forms.renderers import BaseRenderer, EngineMixin
from django.template.backends.django import DjangoTemplates
from django.utils.functional import cached_property

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))


class NHSUKFrontendRenderer(EngineMixin, BaseRenderer):
    backend = DjangoTemplates

    @cached_property
    def engine(self):
        return self.backend(
            {
                "APP_DIRS": True,
                "DIRS": [
                    ROOT_DIR + "/templates",  # wagtailnhsukfrontend/forms
                    django.__path__[0] + "/forms/templates",  # base django forms
                ],
                "NAME": "wagtailnhsukfrontendforms",
                "OPTIONS": {},
            }
        )
