# Generated by Django 5.0 on 2024-01-21 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0009_alter_update_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='update',
            options={'ordering': ('-added_date',), 'verbose_name': 'Обновление', 'verbose_name_plural': 'Обновления'},
        ),
        migrations.RemoveField(
            model_name='update',
            name='image',
        ),
    ]
