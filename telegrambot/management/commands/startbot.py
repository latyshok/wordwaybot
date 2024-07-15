import logging

from django.conf import settings
from django.core.management import BaseCommand
from telegram import Update
from telegram.ext import ApplicationBuilder

from telegrambot.services.bot import set_handlers, post_init, post_shutdown


class Command(BaseCommand):
    def handle(self, *args, **options):
        logging.basicConfig(
            level=logging.INFO,
            handlers=[logging.StreamHandler()],
        )

        app = (ApplicationBuilder()
               .token(settings.TELEGRAM.token)
               .post_shutdown(post_shutdown)
               .post_init(post_init))

        app = app.build()

        set_handlers(app)

        app.run_polling(allowed_updates=Update.ALL_TYPES)
