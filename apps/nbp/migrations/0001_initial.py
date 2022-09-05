# Generated by Django 3.2.15 on 2022-09-05 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ExchangeRate",
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
                ("date", models.DateField(verbose_name="date")),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=60, verbose_name="amount"
                    ),
                ),
                (
                    "currency_input",
                    models.CharField(
                        choices=[
                            ("PLN", "Polish Zloty"),
                            ("USD", "US Dollar"),
                            ("EUR", "Euro"),
                            ("CHF", "CHF"),
                            ("JPY", "Japanese Yen"),
                        ],
                        max_length=3,
                        verbose_name="currency input",
                    ),
                ),
                (
                    "currency_output",
                    models.CharField(
                        choices=[
                            ("PLN", "Polish Zloty"),
                            ("USD", "US Dollar"),
                            ("EUR", "Euro"),
                            ("CHF", "CHF"),
                            ("JPY", "Japanese Yen"),
                        ],
                        max_length=3,
                        verbose_name="currency output",
                    ),
                ),
            ],
        ),
    ]