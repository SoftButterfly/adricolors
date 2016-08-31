from django.utils.translation import ugettext as _
from django.db import models


class Slide(models.Model):
    title = models.CharField(
        _("title"),
        max_length=128,
    )

    summary = models.CharField(
        _("summary"),
        max_length=256,
    )

    background = models.ImageField(
        _("background"),
    )

    coa_text = models.CharField(
        _("text"),
        max_length=32,
    )

    registration_date = models.DateTimeField(
        _("registration date"),
        editable=False,
    )

    last_modification = models.DateTimeField(
        _("Last modification"),
        editable=False,
    )

    start_exhibition_date = models.DateTimeField(
        _("start of exhibition"),
    )

    end_exhibition_date = models.DateTimeField(
        _("end of exhibition"),
    )

    class Meta:
        verbose_name = _("Slide")
        verbose_name_plural = _("Slides")

    def __str__(self):
        if self.title == "":
            return _("Unnamed slide")

        return "Slide {0:}".format(self.title)


class Service(models.Model):
    name = models.CharField(
        _("name"),
        max_length=128,
    )

    summary = models.CharField(
        _("summary"),
        max_length=256,
    )

    picture = models.ImageField(
        _("background"),
        default=None
    )

    registration_date = models.DateTimeField(
        _("registration date"),
        editable=False,
    )

    last_modification = models.DateTimeField(
        _("Last modification"),
        editable=False,
    )

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        if self.title == "":
            return _("Unnamed service")

        return "Service of {0:}".format(self.name.title())
