from abc import ABC, abstractmethod

from telegram import Update
from telegram.ext import CallbackContext

from telegrambot.services.user import update_or_create_user


class BaseCallback(ABC):
    def __init__(self):
        self.user = None

    async def __call__(self, update: Update, context: CallbackContext):
        if update.effective_user and not update.effective_user.is_bot:
            user, created = await update_or_create_user(update.effective_user)
            self.user = user
        await self.handle(update, context)

    @classmethod
    def as_callback(cls):
        return cls()

    @abstractmethod
    async def handle(self, update: Update, context: CallbackContext):
        pass
