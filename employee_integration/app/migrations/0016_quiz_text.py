# Generated by Django 3.2.2 on 2021-10-27 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_question_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='text',
            field=models.CharField(default='Описание квеста', max_length=600, verbose_name='Описание квеста'),
            preserve_default=False,
        ),
    ]
