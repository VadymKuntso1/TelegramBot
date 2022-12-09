from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from   telegram import Update 


contact1: False      
def help1 (update=Update, context=CallbackContext):
    chat_id = update.message.chat_id
    update.message.reply_text("""
help - list of commands
contact - Send "Hi!" to me


You chat id :
"""+str(chat_id))
    
#Unknow commands
def echo (update=Update, context=CallbackContext):    
    chat_id1='602274245'
    global  contact1
    if contact1:
        update.message.reply_text("Thank's for you letter")
        contact1 = False
        context.bot.send_message(chat_id1, text=f"{update.message.text}\n \n\n\n Name:{update.message.from_user}")
    else:      
        update.message.reply_text("Sorry, I don't know this command: '"+update.message.text+"'")

     
#Contact commands  
def contact (update=Update, context=CallbackContext):
    try:
        global  contact1
        contact1 = True
        update.message.reply_text("White you message")
        dispatcher = updater.dispatcher
        updater =  Updater("5222512184:AAEc2sILA6AqhvwKv0aYZIROZQ5cvfJfurc")
        update.message.reply_text(dispatcher)
    except(NameError):
        print('Error in contact')



    
def start(update=Update, context=CallbackContext):
    update.message.reply_text("""This is my own bot
/help - to, oddly enough, get help :D

He can work with bd in previous project

Also, you can send me a message""") 


def main():
    try:
        updater =  Updater("5222512184:AAEc2sILA6AqhvwKv0aYZIROZQ5cvfJfurc")
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler("help", help1))
        dispatcher.add_handler(CommandHandler("contact", contact))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
        updater.start_polling()
        updater.idle()
    except (NameError):
        print('Error in main')
main()
