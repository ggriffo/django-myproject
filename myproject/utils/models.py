# Create your models here.
from __future__ import unicode_literals import urlparse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from utils.models import UrlMixin
from utils.models import CreationModificationMixin
from utils.models import MetaTagsMixin
from django.contrib.sites.models import Site
from django.config import settings

class Idea(UrlMixin, CreationModificationMixin, MetaTagsMixin):
    title = models.CharField(_("Title"), max_length = 200)
    content = models.CharField(_("Content"))

class Meta:
    verbose_name = _("Idea")
    verbose_name_plural = _("Ideas")

def __str__(self):
    return self.title