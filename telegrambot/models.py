from django.db import models
from django.db.models import TextChoices


class TimestampModel(models.Model):
    created_at = models.DateTimeField('дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('дата обновления', auto_now=True)

    class Meta:
        abstract = True


class PrivateChatMemberStatus(TextChoices):
    MEMBER = 'member', 'Бот активен в личном чате с пользователем'
    BANNED = 'kicked', 'Бот был заблокирован пользователем в личном чате'


class TelegramUser(TimestampModel):
    telegram_id = models.BigIntegerField(primary_key=True)
    chat_member_status = models.CharField('статус', max_length=50, choices=PrivateChatMemberStatus.choices,
                                          default=PrivateChatMemberStatus.MEMBER)
    username = models.CharField('пользователь', max_length=255)
    first_name = models.CharField('имя', max_length=50)
    last_name = models.CharField('фамилия', max_length=50, null=True, blank=True)
    language_code = models.CharField('язык', max_length=20, blank=True, null=True)
    is_premium = models.BooleanField('премиум', default=False)
    added_to_attachment_menu = models.BooleanField('добавил бота в attachment menu', default=False)

    def __str__(self):
        name = f'{self.first_name} {self.last_name or ""}'.strip()
        return f'{name} ({self.pk})'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
