from django.utils.translation import ugettext as _
from django.contrib import admin
from home.models import Slide
from home.models import Service


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'start_exhibition_date',
        'end_exhibition_date',
    )

    fieldsets = (
        (
            _("Slide content"),
            {
                "fields": (
                    "title",
                    "summary",
                    "background",
                ),
            }
        ),
        (
            _("Call of action"),
            {
                "fields": (
                    "coa_text",
                ),
            }
        ),
        (
            _("Exhibition"),
            {
                "fields": (
                    "start_exhibition_date",
                    "end_exhibition_date",
                ),
            }
        ),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'summary',
    )

    fieldsets = (
        (
            _("Slide content"),
            {
                "fields": (
                    "name",
                    "summary",
                    "picture",
                ),
            }
        ),
    )
