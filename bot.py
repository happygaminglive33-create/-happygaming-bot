from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8874099044:AAG8oFYSXErVU5rBVvzlQxlU8ns58vixU8c"
GROUP_LINK = "https://t.me/happygaming70"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("😊 Happy / خوش دبائیں", callback_data='happy')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Aapki tasveer ke saath salam
    caption = (
        "السلام علیکم ورحمتہ اللہ وبرکاتہ! 🤲\n\n"
        "میں ہوں Happy Gaming والا! 😊\n"
        "Welcome to my Birthday Bot 🎂\n\n"
        "براہ مہربانی نیچے والا Happy کا بٹن دبائیں 👇\n"
        "Please press Happy button below 👇"
    )
    # photo.jpg ko bhejna
    with open("photo.jpg", "rb") as photo_file:
        await update.message.reply_photo(photo=photo_file, caption=caption, reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'happy':
        await query.message.reply_text(
            f"🎉 Happy! بہت مبارک ہو 🎂\n\n"
            f"یہ رہا آپ کا گروپ لنک 👇\n"
            f"Here is your group link 👇\n\n"
            f"{GROUP_LINK}\n\n"
            f"Join kar lein ❤️"
        )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_click))
print("Bot Chal Raha Hai...")
app.run_polling()
