# Generated by Django 4.2 on 2023-04-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("virtance", "0003_alter_virtance_event_virtanceerror"),
    ]

    operations = [
        migrations.AddField(
            model_name="virtance",
            name="is_recovery_mode",
            field=models.BooleanField(default=False),
        ),
    ]