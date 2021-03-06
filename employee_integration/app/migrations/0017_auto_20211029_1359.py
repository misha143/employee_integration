# Generated by Django 3.2.2 on 2021-10-29 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_quiz_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_input_question',
            field=models.BooleanField(default=False, verbose_name='Отметьте, если ответ на этот вопрос пользователь вводит сам'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='correct',
            field=models.BooleanField(blank=True, help_text='Выберите 1 правильный ответ для 1 вопроса', verbose_name='Правильный?'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(max_length=1000, verbose_name='Текст ответа'),
        ),
    ]
