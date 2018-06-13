from telegram.ext import Updater, CommandHandler
from bot_logger import log
from config import TOKEN
from requests import get
FOAAS_BASE_URL = 'https://www.foaas.com'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


def start_bot() -> None:
    """Connects the bot to Telegram."""

    log.info("The bot have started to move!")
    dispatcher.add_handler(CommandHandler('start', start_handler))
    dispatcher.add_handler(CommandHandler('help', help_handler))
    dispatcher.add_handler(CommandHandler('fuckyou', fuck_you_handler))

    updater.start_polling()


def start_handler(bot, update) -> None:
    """Handler for the /start command."""

    log.info(f"User {update.message.from_user.username} ran /start.")
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Send a friendly "Fuck You!" to your friends! Type /help for a list of fucking commands'
    )


def fuck_you_handler(bot, update) -> None:
    """Handler for the fuckyou command."""

    log.info(f"User {update.message.from_user.username} ran /fuckyou.")
    username: str = update.message.from_user.username

    # TODO Query FOAAS API for string
    # TODO send string back in chat message


def help_handler(bot, update) -> None:
    """Handler for the /help command."""

    log.info(f"User {update.message.from_user.username} ran /help.")
    bot.send_message(
        chat_id=update.message.chat_id,
        text=(
            "I'm an interface to the FOAAS API. Fuck you.\n"
            "Here are some commands I can do:\n\n"
            "/fuckyou\n"
        )
    )


if __name__ == '__main__':
    start_bot()
