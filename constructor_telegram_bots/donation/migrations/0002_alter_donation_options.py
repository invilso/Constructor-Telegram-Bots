# Generated by Django 4.2.3 on 2023-08-02 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donation',
            options={'ordering': ['-date'], 'verbose_name': 'Пожертвование', 'verbose_name_plural': 'Пожертвования'},
        ),
    ]
