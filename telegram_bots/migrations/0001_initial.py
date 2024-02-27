# Generated by Django 5.0.2 on 2024-02-27 02:43

import django.db.models.deletion
import telegram_bots.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('x', models.FloatField(default=0, verbose_name='Координата X')),
                ('y', models.FloatField(default=0, verbose_name='Координата Y')),
                ('interval', models.PositiveSmallIntegerField(choices=[(1, '1 день'), (3, '3 дня'), (7, '7 дней'), (14, '14 дней'), (28, '28 дней')], verbose_name='Интервал')),
            ],
            options={
                'verbose_name': 'Фоновая задача',
                'verbose_name_plural': 'Фоновые задачи',
                'db_table': 'telegram_bot_background_task',
            },
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('x', models.FloatField(default=0, verbose_name='Координата X')),
                ('y', models.FloatField(default=0, verbose_name='Координата Y')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
                'db_table': 'telegram_bot_command',
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('x', models.FloatField(default=0, verbose_name='Координата X')),
                ('y', models.FloatField(default=0, verbose_name='Координата Y')),
            ],
            options={
                'verbose_name': 'Условие',
                'verbose_name_plural': 'Условия',
                'db_table': 'telegram_bot_condition',
            },
        ),
        migrations.CreateModel(
            name='BackgroundTaskAPIRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='URL-адрес')),
                ('method', models.CharField(choices=[('get', 'GET'), ('post', 'POST'), ('put', 'PUT'), ('patch', 'PATCH'), ('delete', 'DELETE')], default='get', max_length=6, verbose_name='Метод')),
                ('headers', models.JSONField(blank=True, null=True, verbose_name='Заголовки')),
                ('body', models.JSONField(blank=True, null=True, verbose_name='Данные')),
                ('background_task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='api_request', to='telegram_bots.backgroundtask', verbose_name='Фоновая задача')),
            ],
            options={
                'verbose_name': 'API-запрос фоновой задачи',
                'verbose_name_plural': 'API-запросы фоновых задач',
                'db_table': 'telegram_bot_background_task_api_request',
            },
        ),
        migrations.CreateModel(
            name='CommandAPIRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='URL-адрес')),
                ('method', models.CharField(choices=[('get', 'GET'), ('post', 'POST'), ('put', 'PUT'), ('patch', 'PATCH'), ('delete', 'DELETE')], default='get', max_length=6, verbose_name='Метод')),
                ('headers', models.JSONField(blank=True, null=True, verbose_name='Заголовки')),
                ('body', models.JSONField(blank=True, null=True, verbose_name='Данные')),
                ('command', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='api_request', to='telegram_bots.command', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'API-запрос команды',
                'verbose_name_plural': 'API-запросы команд',
                'db_table': 'telegram_bot_command_api_request',
            },
        ),
        migrations.CreateModel(
            name='CommandDatabaseRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField(verbose_name='Данные')),
                ('command', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='database_record', to='telegram_bots.command', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'Запись в БД команды',
                'verbose_name_plural': 'Записи в БД команд',
                'db_table': 'telegram_bot_command_database_record',
            },
        ),
        migrations.CreateModel(
            name='CommandFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to=telegram_bots.models.upload_command_file_path, verbose_name='Файл')),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='telegram_bots.command', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'Файл команды',
                'verbose_name_plural': 'Файлы команд',
                'db_table': 'telegram_bot_command_file',
            },
        ),
        migrations.CreateModel(
            name='CommandImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=telegram_bots.models.upload_command_image_path, verbose_name='Изображение')),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='telegram_bots.command', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'Изображение команды',
                'verbose_name_plural': 'Изображения команд',
                'db_table': 'telegram_bot_command_image',
            },
        ),
        migrations.CreateModel(
            name='CommandKeyboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('default', 'Обычный'), ('inline', 'Встроенный'), ('payment', 'Платёжный')], default='default', max_length=7, verbose_name='Режим')),
                ('command', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='keyboard', to='telegram_bots.command', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'Клавиатура команды',
                'verbose_name_plural': 'Клавиатуры команд',
                'db_table': 'telegram_bot_command_keyboard',
            },
        ),
        migrations.CreateModel(
            name='CommandKeyboardButton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Ряд')),
                ('text', models.TextField(max_length=512, verbose_name='Текст')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL-адрес')),
                ('keyboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buttons', to='telegram_bots.commandkeyboard', verbose_name='Клавиатура')),
            ],
            options={
                'verbose_name': 'Кнопка клавиатуры команды',
                'verbose_name_plural': 'Кнопки клавиатур команд',
                'db_table': 'telegram_bot_command_keyboard_button',
            },
        ),
        migrations.CreateModel(
            name='CommandKeyboardButtonConnection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_handle_position', models.CharField(choices=[('left', 'Слева'), ('right', 'Справа')], default='left', max_length=5, verbose_name='Стартовая позиция коннектора')),
                ('target_handle_position', models.CharField(choices=[('left', 'Слева'), ('right', 'Справа')], default='right', max_length=5, verbose_name='Окончательная позиция коннектора')),
                ('button', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connected_commands', to='telegram_bots.commandkeyboardbutton', verbose_name='Кнопка')),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connected_keyboard_buttons', to='telegram_bots.command', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'Соединение между кнопкой и командой',
                'verbose_name_plural': 'Соединения между кнопкой и командой',
                'db_table': 'telegram_bot_command_keyboard_button_connection',
            },
        ),
        migrations.CreateModel(
            name='CommandMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=4096, verbose_name='Текст')),
                ('command', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='telegram_bots.command', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'Сообщение команды',
                'verbose_name_plural': 'Сообщения команд',
                'db_table': 'telegram_bot_command_message',
            },
        ),
        migrations.CreateModel(
            name='CommandSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_reply_to_user_message', models.BooleanField(default=False, verbose_name='Ответить на сообщение пользователя')),
                ('is_delete_user_message', models.BooleanField(default=False, verbose_name='Удалить сообщение пользователя')),
                ('is_send_as_new_message', models.BooleanField(default=False, verbose_name='Отправить сообщение как новое')),
                ('command', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='telegram_bots.command', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'Настройки команды',
                'verbose_name_plural': 'Настройки команд',
                'db_table': 'telegram_bot_command_settings',
            },
        ),
        migrations.CreateModel(
            name='CommandTrigger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Текст')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
                ('command', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='trigger', to='telegram_bots.command', verbose_name='Команда')),
            ],
            options={
                'verbose_name': 'Триггер команды',
                'verbose_name_plural': 'Триггеры команд',
                'db_table': 'telegram_bot_command_trigger',
            },
        ),
        migrations.CreateModel(
            name='ConditionPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('+', 'Положительный'), ('-', 'Отрицательный')], max_length=1, verbose_name='Тип')),
                ('first_value', models.CharField(max_length=255, verbose_name='Первое значение')),
                ('operator', models.CharField(choices=[('==', 'Равно'), ('!=', 'Не равно'), ('>', 'Больше'), ('>=', 'Больше или равно'), ('<', 'Меньше'), ('<=', 'Меньше или равно')], max_length=2, verbose_name='Оператор')),
                ('second_value', models.CharField(max_length=255, verbose_name='Второе значение')),
                ('next_part_operator', models.CharField(blank=True, choices=[('&&', 'И'), ('||', 'ИЛИ')], max_length=2, null=True, verbose_name='Оператор для следующей части')),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='telegram_bots.condition', verbose_name='Условие')),
            ],
            options={
                'verbose_name': 'Часть условия',
                'verbose_name_plural': 'Части условий',
                'db_table': 'telegram_bot_condition_part',
            },
        ),
        migrations.CreateModel(
            name='TelegramBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='@username')),
                ('api_token', models.CharField(max_length=50, unique=True, validators=[telegram_bots.models.validate_api_token], verbose_name='API-токен')),
                ('storage_size', models.PositiveBigIntegerField(default=41943040, verbose_name='Размер хранилища')),
                ('is_private', models.BooleanField(default=False, verbose_name='Приватный')),
                ('is_enabled', models.BooleanField(default=False, verbose_name='Включён')),
                ('is_loading', models.BooleanField(default=False, verbose_name='Загружаеться')),
                ('added_date', models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telegram_bots', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Telegram бота',
                'verbose_name_plural': 'Telegram боты',
                'db_table': 'telegram_bot',
            },
        ),
        migrations.AddField(
            model_name='condition',
            name='telegram_bot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conditions', to='telegram_bots.telegrambot', verbose_name='Telegram бот'),
        ),
        migrations.AddField(
            model_name='command',
            name='telegram_bot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commands', to='telegram_bots.telegrambot', verbose_name='Telegram бот'),
        ),
        migrations.AddField(
            model_name='backgroundtask',
            name='telegram_bot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='background_tasks', to='telegram_bots.telegrambot', verbose_name='Telegram бот'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.PositiveBigIntegerField(verbose_name='Telegram ID')),
                ('full_name', models.CharField(max_length=129, verbose_name='Имя и фамилия')),
                ('is_allowed', models.BooleanField(default=False, verbose_name='Разрешён')),
                ('is_blocked', models.BooleanField(default=False, verbose_name='Заблокирован')),
                ('last_activity_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата последней активности')),
                ('activated_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата активации')),
                ('telegram_bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='telegram_bots.telegrambot', verbose_name='Telegram бот')),
            ],
            options={
                'verbose_name': 'Пользователя',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'telegram_bot_user',
            },
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('value', models.TextField(max_length=2048, verbose_name='Значение')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('telegram_bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variables', to='telegram_bots.telegrambot', verbose_name='Telegram бот')),
            ],
            options={
                'verbose_name': 'Переменная',
                'verbose_name_plural': 'Переменные',
                'db_table': 'telegram_bot_variable',
            },
        ),
    ]
