import re
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler
from database.db_manager import db_manager
from utils.constants import CONTATO_NOME, CONTATO_EMAIL, CONTATO_MENSAGEM


async def iniciar_contato(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Para entrarmos em contato, precisamos de algumas informações.\n\n"
        "Por favor, digite seu nome completo:"
    )
    return CONTATO_NOME


async def processar_contato_nome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['nome'] = update.message.text
    
    await update.message.reply_text(
        f"Obrigado, {context.user_data['nome']}!\n\n"
        "Agora, por favor, digite seu e-mail para contato:"
    )
    return CONTATO_EMAIL


async def processar_contato_email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    email = update.message.text
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        await update.message.reply_text(
            "O e-mail informado parece inválido. Por favor, digite um e-mail válido:"
        )
        return CONTATO_EMAIL
    
    context.user_data['email'] = email
    
    produto_msg = ""
    if 'produto_interesse' in context.user_data:
        produto_msg = f"Vejo que você demonstrou interesse no produto: {context.user_data['produto_interesse']}.\n\n"
    
    await update.message.reply_text(
        f"Perfeito! {produto_msg}"
        "Por último, descreva sua solicitação ou dúvida:"
    )
    return CONTATO_MENSAGEM


async def processar_contato_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['mensagem'] = update.message.text
    user_id = update.effective_user.id
    
    if 'produto_interesse' in context.user_data:
        context.user_data['mensagem'] += f"\n\nProduto de interesse: {context.user_data['produto_interesse']}"
    
    if db_manager.save_contact(
        user_id, 
        context.user_data['nome'], 
        context.user_data['email'], 
        context.user_data['mensagem']
    ):
        keyboard = [
            [InlineKeyboardButton("Menu Principal", callback_data='menu_principal')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            f"Obrigado, {context.user_data['nome']}!\n\n"
            "Sua solicitação foi registrada com sucesso. Nossa equipe entrará em contato em breve através do e-mail fornecido.",
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            "Desculpe, ocorreu um erro ao salvar sua solicitação. Por favor, tente novamente mais tarde."
        )
    
    context.user_data.clear()
    return ConversationHandler.END