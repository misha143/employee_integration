# Generated by Django 3.2.2 on 2021-09-23 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20210923_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='valid_until',
        ),
    ]