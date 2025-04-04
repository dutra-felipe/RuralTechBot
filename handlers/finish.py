from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes
from telegram.ext import ConversationHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    
    await update.message.reply_text(
        "Bem-vindo! Para iniciar um novo atendimento, utilize os comandos disponíveis.\n\nDigite /start para começar.",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

async def finalizar_atendimento(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    
    await update.message.reply_text(
        "Atendimento encerrado. Para iniciar um novo atendimento, utilize o comando /start.",
        reply_markup=ReplyKeyboardRemove()
    )
    
    return ConversationHandler.END
