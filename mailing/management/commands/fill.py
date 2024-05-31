from django.core.management import BaseCommand

from mailing.cron import send_mailing_email
from mailing.models import Settings


class Command(BaseCommand):
    mailing = Settings.objects.all().first()

    def handle(self, *args, **options):
        send_mailing_email(self.mailing)
