# Generated by Django 5.1 on 2024-09-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_stockentry_delete_moodentry"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stockentry",
            name="price",
            field=models.IntegerField(),
        ),
    ]
