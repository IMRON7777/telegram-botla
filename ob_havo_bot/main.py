from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from methods import *

updater = Updater(token= '5039690237:AAEp18upb68jueG9uHcZ_61Ifb-OgOIB8Yg')


dispatcher = updater.dispatcher

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start',start)],
     states={
         1:[MessageHandler(Filters.regex("^(Toshkent)$"), toshkent),
            MessageHandler(Filters.regex("^(Toshkent viloyati)$"), toshkent_viloyati),
            MessageHandler(Filters.regex("^(Sirdaryo)$"), sirdaryo),
            MessageHandler(Filters.regex("^(Jizzax)$"), jizzax),
            MessageHandler(Filters.regex("^(Samarqand)$"),samarqand),
            ]

     },
    fallbacks= [MessageHandler(Filters.text, start)]

)
dispatcher.add_handler(conv_handler)
updater.start_polling()

print("Hammasi yaxshi bot ishladi")