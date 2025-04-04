from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.constants import FAQ, ESCOLHA, FINALIZAR_ATENDIMENTO


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        user = update.effective_user
        message = update.message
    elif update.callback_query:
        user = update.callback_query.from_user
        message = update.callback_query.message
        await update.callback_query.answer()
    else:
        return

    keyboard = [
        [InlineKeyboardButton("📋 Catálogo de Produtos", callback_data='produtos')],
        [InlineKeyboardButton("⏰ Horário de Atendimento", callback_data='horario')],
        [InlineKeyboardButton("🔍 Sobre a Empresa", callback_data='sobre')],
        [InlineKeyboardButton("📍 Localização", callback_data='endereco')],
        [InlineKeyboardButton("📱 Contato", callback_data='contato')],
        [InlineKeyboardButton("💻 Site", callback_data='site')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await message.reply_text(
        f"Olá, {user.first_name}! Seja bem-vindo(a) ao atendimento da RuralTech.\n\n"
        "Somos especialistas em soluções tecnológicas para agricultura. Como posso te ajudar hoje?",
        reply_markup=reply_markup
    )
    return ESCOLHA

async def finalizar_atendimento(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    
    keyboard = [
        [InlineKeyboardButton("🔄 Iniciar Novo Atendimento", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    message_text = "Atendimento encerrado. Para iniciar um novo atendimento, utilize o botão abaixo."
    
    if update.callback_query:
        await update.callback_query.message.edit_text(message_text, reply_markup=reply_markup)
    elif update.message:
        await update.message.reply_text(message_text, reply_markup=reply_markup)
    
    return FINALIZAR_ATENDIMENTO

async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Menu Principal", callback_data='menu_principal')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Aqui estão os comandos disponíveis:\n\n"
        "/start - Iniciar a conversa e ver o menu principal\n"
        "/ajuda - Ver esta mensagem de ajuda\n"
        "/horario - Verificar nosso horário de funcionamento\n"
        "/site - Visitar nosso site\n"
        "/sobre - Informações sobre a empresa\n"
        "/contato - Formulário para entrar em contato\n"
        "/endereco - Obter informações sobre nossa localização\n"
        "/produtos - Ver catálogo de produtos\n"
        "/feedback - Enviar sua opinião sobre nosso atendimento\n\n"
        "Você também pode simplesmente digitar sua dúvida em linguagem natural.",
        reply_markup=reply_markup
    )

async def produtos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Sensor de Umidade", callback_data='produto_sensor')],
        [InlineKeyboardButton("Drone para Mapeamento", callback_data='produto_drone')],
        [InlineKeyboardButton("Software de Gestão", callback_data='produto_software')],
        [InlineKeyboardButton("⬅️ Voltar ao Menu Principal", callback_data='menu_principal')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Confira nossos produtos inovadores para o agronegócio:",
        reply_markup=reply_markup
    )
    return ESCOLHA

async def horario(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Menu Principal", callback_data='menu_principal')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(FAQ["horario"], reply_markup=reply_markup)

async def site(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Menu Principal", callback_data='menu_principal')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(FAQ["site"], reply_markup=reply_markup)

async def sobre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Menu Principal", callback_data='menu_principal')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(FAQ["sobre"], reply_markup=reply_markup)

async def endereco(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Menu Principal", callback_data='menu_principal')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(FAQ["endereco"], reply_markup=reply_markup)
