# Generated by Django 4.2.3 on 2023-09-15 09:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("image", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="arch",
            field=models.CharField(
                choices=[("x86_64", "X64"), ("aarch64", "ARM64")],
                default="x86_64",
                max_length=50,
            ),
        ),
    ]