# Generated by Django 5.0.6 on 2024-05-17 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=128, verbose_name='Слово')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Изображение')),
                ('translation_options', models.TextField(verbose_name='Варианты перевода')),
                ('answer', models.CharField(max_length=128, verbose_name='Перевод')),
            ],
            options={
                'verbose_name': 'Карточки вопросов',
                'verbose_name_plural': 'Карточки вопроса',
            },
        ),
    ]