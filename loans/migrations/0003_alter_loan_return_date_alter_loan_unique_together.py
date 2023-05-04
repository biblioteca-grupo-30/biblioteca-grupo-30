# Generated by Django 4.2 on 2023-05-04 13:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("exemplaries", "0002_exemplary_default_loan_duration"),
        ("loans", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loan",
            name="return_date",
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterUniqueTogether(
            name="loan",
            unique_together={("exemplary", "user")},
        ),
    ]
