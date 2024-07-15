from typing import Any

from telegram import User, Chat

from telegrambot.models import TelegramUser


async def update_or_create_user(user: User) -> tuple[Any, bool]:
    defaults = user.to_dict()
    del defaults['id']

    return await TelegramUser.objects.aupdate_or_create(
        telegram_id=user.id,
        defaults={
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'language_code': user.language_code,
            'is_premium': user.is_premium,
            'added_to_attachment_menu': user.added_to_attachment_menu if user.added_to_attachment_menu else False,
        },
    )
