# Generated by Django 4.2.3 on 2023-11-12 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("firewall", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FirewallError",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("event", models.CharField(blank=True, max_length=40, null=True)),
                ("message", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("firewall", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="firewall.firewall")),
            ],
            options={
                "verbose_name": "Firewall Error",
                "verbose_name_plural": "Firewalls Errors",
                "ordering": ["-id"],
            },
        ),
    ]
