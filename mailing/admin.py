from django.contrib import admin

from mailing.models import Settings, Attempt


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('first_mailing_date', 'status',)
    list_filter = ('first_mailing_date', 'status',)


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('last_attempt_date', 'status',)
    list_filter = ('last_attempt_date', 'status',)
