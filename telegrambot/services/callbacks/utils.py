import json

from telegram import Update
from telegram.constants import ChatType
from telegram.ext import CallbackContext

from telegrambot.models import TelegramUser


async def debug(update: Update, context: CallbackContext):
    print(json.dumps(update.to_dict(), indent=5, ensure_ascii=False))


async def update_chat_member_status(update: Update, context: CallbackContext):
    if update.my_chat_member.chat.type == ChatType.PRIVATE:
        await TelegramUser.objects.aupdate(
            telegram_id=update.effective_user.id,
            chat_member_status=update.my_chat_member.new_chat_member.status
        )
