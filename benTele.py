from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
    update.message.reply_text("I am Ben's bot, nice to meet you")

def convert_uppercase(bot, update):
    update.message.reply_text(update.message.text.upper())

def main():

    updater = Updater('744158440:AAGvuyeMIAx4CPnUpAhdORXgLHM1bfNaC5o')
    dispatcher = updater.dispatcher
    print("bot started")


    start_handler = CommandHandler('start', start)
    upper_case_handler = MessageHandler(Filters.text, convert_uppercase)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(upper_case_handler)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
