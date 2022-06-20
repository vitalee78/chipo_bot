import logging.config
from datetime import datetime
from telegram import Bot
from telegram import Update
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

from config import TG_TOKEN
from config import LOGGING
from utils import logger_factory

logging.config.dictConfig(LOGGING)
logger = logging.getLogger('')
debug_requests = logger_factory(logger=logger)


@debug_requests
def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Привет! Отправь что-нибудь"
    )


@debug_requests
def do_help(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Это учебный бот\n"
             "Список доступных команд\n"
             "Так же я отвечу на любые вопросы"
    )


@debug_requests
def do_echo(bot: Bot, update: Update):
    chat_id = update.message.chat_id
    text = update.message.text
    reply_text = f"Ваш ID = {chat_id}\n\n {text}"
    bot.send_message(
        chat_id=chat_id,
        text=reply_text
    )


@debug_requests
def do_time(bot: Bot, update: Update):
    date_format = '%d-%m-%Y'
    today = datetime.now()
    text = today.strftime(date_format)

    bot.send_message(
        chat_id=update.message.chat_id,
        text=text
    )


def main():
    bot = Bot(token=TG_TOKEN)
    updater = Updater(bot=bot)

    start_handler = CommandHandler("start", do_start)
    help_handler = CommandHandler("help", do_help)
    time_handler = CommandHandler("time", do_time)
    message_handler = MessageHandler(Filters.text, do_echo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(time_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
