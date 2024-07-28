from django.forms import ModelForm

from mailing.models import Settings


class SettingsForm(ModelForm):
    class Meta:
        model = Settings
        fields = [
            'first_mailing_date',
            'frequency',
            'status',
            'message',
            'client',
            ]


class SettingsModeratorForm(ModelForm):
    class Meta:
        model = Settings
        fields = [
            'status',
            ]
