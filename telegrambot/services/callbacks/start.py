from telegram import Update
from telegram.ext import CallbackContext

from telegrambot.services.callbacks.base import BaseCallback

welcome_message = ('Привет, {}! 👋 \n\n'
                   'Я - ваш личный помощник для заучивания английских слов. '
                   'Вместе мы будем изучать новые слова, пополнять словарный запас'
                   ' и делать ваш английский лучше каждый день! 🧠📚\n\n'
                   'Вот несколько команд, которые могут быть полезны:\n\n'
                   '/new - добавить новое слово\n'
                   '/review - повторить слова\n'
                   '/progress - узнать о своем прогрессе\n\n'
                   'Давайте начнем наше увлекательное путешествие в мир английского языка! 🚀')


class Start(BaseCallback):
    async def handle(self, update: Update, context: CallbackContext):
        await update.effective_message.reply_text(text=welcome_message.format(update.message.from_user.first_name))
