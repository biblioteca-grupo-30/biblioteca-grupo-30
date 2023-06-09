# Generated by Django 4.2 on 2023-05-05 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("exemplaries", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Loan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("return_date", models.DateTimeField(blank=True)),
                ("returned_date", models.DateTimeField(blank=True, null=True)),
                ("loan_date", models.DateTimeField(auto_now_add=True)),
                (
                    "exemplary",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exemplaries.exemplary",
                    ),
                ),
            ],
        ),
    ]
