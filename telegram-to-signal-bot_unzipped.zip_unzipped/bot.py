import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
import subprocess

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
SIGNAL_CLI_NUMBER = os.getenv("SIGNAL_CLI_NUMBER")
SIGNAL_RECIPIENT = os.getenv("SIGNAL_RECIPIENT")

async def forward_to_signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text
    sender = update.message.from_user.first_name
    full_message = f"Telegram von {sender}: {message}"
    subprocess.run(["signal-cli", "-u", SIGNAL_CLI_NUMBER, "send", SIGNAL_RECIPIENT, "-m", full_message])

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), forward_to_signal))
    app.run_polling()