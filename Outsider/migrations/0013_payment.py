# Generated by Django 4.2.4 on 2023-09-18 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Outsider", "0012_cart_expday_order_expday"),
    ]

    operations = [
        migrations.CreateModel(
            name="payment",
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
                ("name", models.CharField(max_length=20)),
                ("amount", models.CharField(max_length=20)),
                ("date", models.CharField(max_length=20)),
                ("payment_status", models.CharField(max_length=20)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Outsider.outsiders",
                    ),
                ),
            ],
        ),
    ]
