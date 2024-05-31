from django.contrib import admin

from mailing.models import Settings, Attempt


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('first_mailing_date', 'get_client', 'status',)
    list_filter = ('first_mailing_date', 'status',)

    def get_client(self, obj):
        return ', '.join([p.email for p in obj.client.all()])


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('last_attempt_date', 'status',)
    list_filter = ('last_attempt_date', 'status',)
