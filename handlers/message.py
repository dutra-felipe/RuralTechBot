import re
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.constants import FAQ, BOAS_VINDAS, RESPOSTAS_NAO_ENTENDI


async def processar_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()
    
    if re.search(r'\b(oi|olá|ola|hi|hello|e aí|e ai|hey)\b', texto):
        keyboard = [
            [InlineKeyboardButton("Ver Menu Principal", callback_data='menu_principal')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(random.choice(BOAS_VINDAS), reply_markup=reply_markup)
        return
    
    response_sent = False
    
    for keyword, response in FAQ.items():
        if keyword in texto:
            keyboard = [
                [InlineKeyboardButton("Menu Principal", callback_data='menu_principal')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text(response, reply_markup=reply_markup)
            response_sent = True
            break
    
    if not response_sent:
        keyboard = [
            [InlineKeyboardButton("Ver Menu de Opções", callback_data='menu_principal')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            random.choice(RESPOSTAS_NAO_ENTENDI) + "\n\nOu utilize nosso menu para navegar pelas opções:",
            reply_markup=reply_markup
        )