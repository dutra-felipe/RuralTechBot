from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler
from database.db_manager import db_manager
from utils.constants import FEEDBACK


async def iniciar_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Agradecemos seu interesse em enviar um feedback!\n\n"
        "Por favor, digite sua avaliação sobre nosso atendimento ou produtos:"
    )
    return FEEDBACK


async def processar_feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    feedback = update.message.text
    user_id = update.effective_user.id
    name = update.effective_user.first_name or "Sem nome"
    
    if db_manager.save_feedback(user_id, name, feedback):
        keyboard = [
            [InlineKeyboardButton("Menu Principal", callback_data='menu_principal')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "Obrigado pelo seu feedback! Sua opinião é muito importante para nós e nos ajuda a melhorar nossos serviços.",
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            "Desculpe, ocorreu um erro ao salvar seu feedback. Por favor, tente novamente mais tarde."
        )
    
    return ConversationHandler.END