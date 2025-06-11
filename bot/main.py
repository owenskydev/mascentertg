from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from bot.config import BOT_TOKEN
from bot.handlers import start, button_handler

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()

if __name__ == "__main__":
    main()
