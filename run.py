from telegram.ext import Updater
from bot_logger import log
from config import TOKEN
updater = Updater(token=TOKEN)


def start_bot() -> None:
    """Connects the bot to Telegram."""

    # TODO connect to Telegram here

    log.info("The bot have started to move!")

    raise NotImplementedError


def start_handler(bot, update) -> None:
    """Handler for the /start command."""

    bot.send_message(
        chat_id=update.message.chat_id,
        text='INSERT_MESSAGE_HERE'
    )

def help_handler(bot, update) -> None:
    """Handler for the /help command."""

    bot.send_message(
        chat_id=update.message.chat_id,
        text=(
            "I'm an interface to the FOAAS API. Fuck you.\n"
            "Here are some commands I can do:\n\n"
        )
    )


if __name__ == '__main__':
    start_bot()
