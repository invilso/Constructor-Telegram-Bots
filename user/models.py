from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from utils.other import generate_random_string

from asgiref.sync import sync_to_async
import requests
import string


class UserManager(BaseUserManager):
	def create(self, telegram_id: int, first_name: str, **extra_fields) -> 'User':
		return super().create(telegram_id=telegram_id, first_name=first_name, **extra_fields)

	def create_superuser(self, **fields) -> None:
		raise SyntaxError('Not support to create superuser!')

class User(AbstractBaseUser, PermissionsMixin):
	telegram_id = models.BigIntegerField('Telegram ID', unique=True)
	first_name = models.CharField(_('Имя пользователя'), max_length=64, null=True)
	password = None
	is_staff = models.BooleanField(_('Сотрудник'), default=False)
	confirm_code = models.CharField(max_length=25, unique=True, null=True)
	joined_date = models.DateTimeField(_('Присоединился'), auto_now_add=True)

	USERNAME_FIELD = 'telegram_id'

	objects = UserManager()

	class Meta:
		db_table = 'user'

		verbose_name = _('Пользователя')
		verbose_name_plural = _('Пользователи')

	def generate_confirm_code(self) -> None:
		self.confirm_code = generate_random_string(length=25, chars=string.ascii_letters + string.digits)
		self.save()

	def generate_login_url(self) -> str:
		if not self.confirm_code:
			self.generate_confirm_code()

		return settings.SITE_DOMAIN + f'/login/{self.id}/{self.confirm_code}/'

	@property
	def login_url(self) -> str:
		return self.generate_login_url()

	@property
	async def alogin_url(self) -> str:
		return await sync_to_async(self.generate_login_url)()

	def update_first_name(self) -> None:
		response: requests.Response = requests.get(f'https://api.telegram.org/bot{settings.CONSTRUCTOR_TELEGRAM_BOT_API_TOKEN}/getChat?chat_id={self.telegram_id}')

		if response.status_code == 200:
			first_name: str = response.json()['result']['first_name']

			if self.first_name != first_name:
				self.first_name = first_name
				self.save()

	def __str__(self) -> str:
		return self.first_name if self.first_name else str(self.telegram_id)