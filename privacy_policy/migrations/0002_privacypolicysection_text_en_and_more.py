# Generated by Django 5.0 on 2024-01-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('privacy_policy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='privacypolicysection',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='privacypolicysection',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='privacypolicysection',
            name='text_uk',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='privacypolicysection',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='privacypolicysection',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='privacypolicysection',
            name='title_uk',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
    ]
