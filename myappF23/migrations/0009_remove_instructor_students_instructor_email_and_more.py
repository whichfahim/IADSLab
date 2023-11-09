# Generated by Django 4.2.6 on 2023-11-09 01:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myappF23", "0008_instructor_country_instructor_language"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="instructor",
            name="students",
        ),
        migrations.AddField(
            model_name="instructor",
            name="email",
            field=models.CharField(default="default@example.com", max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="instructor",
            name="user_name",
            field=models.CharField(default="default_name", max_length=50),
            preserve_default=False,
        ),
    ]
