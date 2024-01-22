# Generated by Django 5.0 on 2024-01-22 13:26

import privacy_policy.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicySection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('position', models.IntegerField(blank=True, default=privacy_policy.models.privacy_policy_section_position_default, verbose_name='Позиция')),
                ('last_update_date', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
                'db_table': 'privacy_policy_section',
                'ordering': ('position',),
            },
        ),
    ]
