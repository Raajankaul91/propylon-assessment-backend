# Generated by Django 4.1.9 on 2023-11-27 16:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("file_versions", "0002_alter_filedata_options_fileversion_file_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="fileversion",
            name="is_readable",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="fileversion",
            name="is_writable",
            field=models.BooleanField(default=False),
        ),
    ]
