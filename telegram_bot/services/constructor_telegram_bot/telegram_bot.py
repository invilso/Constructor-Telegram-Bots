from ..core import Bot

from aiogram import Dispatcher
from aiogram.types import Message, BotCommand, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

from user.models import User as DjangoUser

from .middlewares import CreateDjangoUserMiddleware

import asyncio


class ConstructorTelegramBot:
	def __init__(self, api_token: str) -> None:
		self.loop: asyncio.AbstractEventLoop = asyncio.new_event_loop()

		self.bot = Bot(api_token, 'html')
		self.dispatcher = Dispatcher()

	async def start_command(self, message: Message) -> None:
		await self.bot.send_message(chat_id=message.chat.id, text=(
			f'Hello, {message.from_user.full_name}!\n' # type: ignore [union-attr]
			'I am a Telegram bot for Constructor Telegram Bots site.\n'
			'Thank you for being with us ❤️'
		))

		try:
			if message.text.split()[1] == 'login': # type: ignore [union-attr]
				await self.login_command(message)
		except IndexError:
			pass

	async def login_command(self, message: Message) -> None:
		django_user: DjangoUser = await DjangoUser.objects.aget(telegram_id=message.from_user.id) # type: ignore [union-attr]
		django_user_login_url: str = await django_user.alogin_url

		await self.bot.send_message(
			chat_id=message.chat.id,
			text='Click on the button below to login on the site.',
			reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Login', url=django_user_login_url)]]),
		)

	async def setup(self) -> None:
		await self.bot.set_my_commands([
			BotCommand(command='start', description='Starting command'),
			BotCommand(command='login', description='Authorization'),
		])

		self.dispatcher.update.outer_middleware.register(CreateDjangoUserMiddleware())

		self.dispatcher.message.register(self.start_command, Command('start'))
		self.dispatcher.message.register(self.login_command, Command('login'))

	async def start(self) -> None:
		await self.setup()
		await self.dispatcher.start_polling(self.bot, handle_signals=False)
