# Generated by Django 5.0.6 on 2024-05-31 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0007_alter_settings_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='last_attempt_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата последней попытки'),
        ),
    ]
