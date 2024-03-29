# Generated by Django 4.2.4 on 2023-09-17 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Pet_Station", "0003_rename_pets_petdata"),
        ("Outsider", "0010_favorite"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                (
                    "product_name",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("orderdate", models.CharField(max_length=100)),
                ("breed", models.CharField(blank=True, max_length=500, null=True)),
                ("quantity", models.CharField(blank=True, max_length=500, null=True)),
                ("total_price", models.IntegerField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="images")),
                ("category", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "order_status",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Pet_Station.petdata",
                    ),
                ),
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
