from typing import final
from telegram import Update, ReplyKeyboardMarkup
import webscrape as wbs
from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters, ContextTypes
import sentiment_analysis

TOKEN : final = "7815486854:AAF3sfjvyVfUNzojTg7kJlv9FPot5w_KaRU"
BOT_USERNAME : final = "@test1221304422_bot"

async def start_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! How can I help you?")
    return CHOICE

async def news_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("What topic would you like assistance on?")
    return NEWS

async def get_news(update : Update, context : ContextTypes.DEFAULT_TYPE):
    topic = update.message.text
    url = wbs.search_word(topic)
    for i in wbs.get_first_n_articles(url, 10):
        await update.message.reply_text(i)
        # sentiment_analysis.sentiment_analysis()
    return CHOICE

async def track_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("What topic would you like assistance on?")
    return TRACK_UPDATES

async def track_url(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("URL is being tracked.")
    return CHOICE

async def cancel_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("It was nice talking to you!")
    return ConversationHandler.END
    
CHOICE, NEWS, TRACK_UPDATES = range (3)


if __name__ == "__main__":
    print("starting")
    app = Application.builder().token(TOKEN).build()

    conversation_handler = ConversationHandler(entry_points= [CommandHandler("start", start_command)],
                                               states ={
                                                    CHOICE : [CommandHandler("news", news_command), CommandHandler("track_updates", track_url)],
                                                    NEWS : [MessageHandler(filters.Regex("^[\\s\\S]"), get_news)],
                                                    TRACK_UPDATES : [MessageHandler(filters.Regex("^[\\s\\S]"), track_url)]      
                                               },
                                               fallbacks=[CommandHandler("exit", cancel_command)])
    app.add_handler(conversation_handler)
    # app.add_handler(CommandHandler("news", get_news))
    

    print("polling")
    app.run_polling(poll_interval= 3)