# Generated by Django 5.0.1 on 2024-01-24 19:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0009_alter_robot_motor_type_alter_robot_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="robotrun",
            options={"ordering": ["-distance"]},
        ),
    ]
