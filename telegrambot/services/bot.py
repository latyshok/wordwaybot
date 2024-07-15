import logging

from telegram.ext import Application, MessageHandler, filters, CommandHandler, ChatMemberHandler

from telegrambot.services.callbacks.start import Start
from telegrambot.services.callbacks.utils import debug, update_chat_member_status

logger = logging.getLogger('telegrambot')
logger.setLevel(logging.INFO)


def set_handlers(app: Application):
    app.add_handler(CommandHandler('start', Start.as_callback()))
    app.add_handler(MessageHandler(filters.ALL, debug))
    app.add_handler(ChatMemberHandler(update_chat_member_status, ChatMemberHandler.MY_CHAT_MEMBER))


async def post_init(app: Application):
    logger.info('Telegram bot started')


async def post_shutdown(app: Application):
    pass
