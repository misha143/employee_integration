# Generated by Django 3.2.2 on 2021-09-17 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210917_2016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='result',
            options={'verbose_name': 'Результат', 'verbose_name_plural': 'Результаты'},
        ),
    ]