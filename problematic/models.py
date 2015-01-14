from django.db import models
from django.utils.translation import ugettext_lazy as _, pgettext_lazy


# Create your models here.
class Website(models.Model):

    url = models.URLField(
        verbose_name=_(u"URL"),
        unique=True,
        max_length=255)

    description = models.CharField(
        blank=True,
        default="",
        max_length=500)

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        db_index=True)

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        db_index=True)

    class Meta:
        verbose_name = _(u"website")
        verbose_name_plural = _(u"websites")
