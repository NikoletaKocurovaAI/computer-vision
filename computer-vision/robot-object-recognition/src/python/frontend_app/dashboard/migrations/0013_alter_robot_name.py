# Generated by Django 5.0.1 on 2024-01-29 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0012_alter_robot_next_run"),
    ]

    operations = [
        migrations.AlterField(
            model_name="robot",
            name="name",
            field=models.CharField(default="", max_length=128, unique=True),
        ),
    ]