# Generated by Django 4.2.6 on 2023-12-05 09:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("professions", "0002_professionsmodel_is_published_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="professionsmodel",
            options={
                "ordering": ["name"],
                "verbose_name": "профессия",
                "verbose_name_plural": "профессии",
            },
        ),
    ]