# Generated by Django 3.2.2 on 2021-09-24 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_question_valid_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='time_result_done',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Когда прошёл тест? (UTC+5)'),
        ),
    ]
