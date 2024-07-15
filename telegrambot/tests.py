from asgiref.sync import async_to_sync
from django.db import connection, reset_queries
from django.test import TestCase
from telegram import Update, Message, TelegramObject
from telegram.ext import Updater

from telegrambot.models import TelegramUser
from telegrambot.services.user import update_or_create_user


class TelegramBotTestCase(TestCase):
    def test_update_or_create_user(self):
        update_data = {
            "message": {
                "channel_chat_created": False,
                "delete_chat_photo": False,
                "entities": [
                    {
                        "length": 6,
                        "offset": 0,
                        "type": "bot_command"
                    }
                ],
                "group_chat_created": False,
                "supergroup_chat_created": False,
                "text": "/start",
                "chat": {
                    "first_name": "Олег",
                    "id": 340974500,
                    "last_name": "Латыш",
                    "type": "private",
                    "username": "latyshok"
                },
                "date": 1721028641,
                "message_id": 12,
                "from": {
                    "first_name": "Олег",
                    "id": 340974500,
                    "is_bot": False,
                    "is_premium": True,
                    "language_code": "ru",
                    "last_name": "Латыш",
                    "username": "latyshok"
                }
            },
            "update_id": 979873358
        }

        update = Update.de_json(update_data)

        sync_update_or_create_user = async_to_sync(update_or_create_user)
        user, created = sync_update_or_create_user(update.effective_user)

        user: TelegramUser

        self.assertTrue(created)
        self.assertEqual(user.username, update_data['message']['from']['username'])
        self.assertEqual(user.is_premium, update_data['message']['from']['is_premium'])
        self.assertEqual(user.first_name, update_data['message']['from']['first_name'])
        self.assertEqual(user.last_name, update_data['message']['from']['last_name'])

        # Пользователь удалил фамилию в личном кабине и у него закончился премиум

        update_data['update_id'] += 1
        update_data['message']['from']['is_premium'] = False
        del update_data['message']['from']['last_name']

        update = Update.de_json(update_data)
        user, created = sync_update_or_create_user(update.effective_user)

        self.assertFalse(created)
        self.assertEqual(user.last_name, None)
        self.assertEqual(user.is_premium, False)
