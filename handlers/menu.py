from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.constants import ESCOLHA, FAQ, PRODUTOS
from handlers.command import start, finalizar_atendimento


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'start':
        return await start(update, context)
    
    if query.data == 'finalizar_atendimento':
        return await finalizar_atendimento(update, context)

    if query.data == 'produtos':
        keyboard = [
            [InlineKeyboardButton("Sensor de Umidade", callback_data='produto_sensor')],
            [InlineKeyboardButton("Drone para Mapeamento", callback_data='produto_drone')],
            [InlineKeyboardButton("Software de Gestão", callback_data='produto_software')],
            [InlineKeyboardButton("⬅️ Voltar ao Menu Principal", callback_data='menu_principal')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("Selecione um produto para saber mais:", reply_markup=reply_markup)
    
    elif query.data.startswith('produto_'):
        produto_id = query.data.split('_')[1]
        produto = PRODUTOS[produto_id]
        
        keyboard = [
            [InlineKeyboardButton("⬅️ Voltar aos Produtos", callback_data='produtos')],
            [InlineKeyboardButton("📲 Solicitar Orçamento", callback_data=f'orcamento_{produto_id}')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        produto_texto = f"*{produto['nome']}*\n\n" \
                       f"*Preço:* {produto['preco']}\n\n" \
                       f"*Descrição:* {produto['descricao']}\n\n" \
                       f"Interessado? Clique em 'Solicitar Orçamento' abaixo!"
        
        await query.edit_message_text(produto_texto, reply_markup=reply_markup, parse_mode='Markdown')
    
    elif query.data.startswith('orcamento_'):
        produto_id = query.data.split('_')[1]
        context.user_data['produto_interesse'] = PRODUTOS[produto_id]['nome']
        
        keyboard = [
            [InlineKeyboardButton("⬅️ Voltar", callback_data='produtos')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            "Para solicitar um orçamento, por favor, envie seus dados através do formulário de contato.\n\n"
            "Digite /contato para iniciar o processo.",
            reply_markup=reply_markup
        )
    
    elif query.data == 'menu_principal':
        keyboard = [
            [InlineKeyboardButton("📋 Catálogo de Produtos", callback_data='produtos')],
            [InlineKeyboardButton("⏰ Horário de Atendimento", callback_data='horario')],
            [InlineKeyboardButton("🔍 Sobre a Empresa", callback_data='sobre')],
            [InlineKeyboardButton("📍 Localização", callback_data='endereco')],
            [InlineKeyboardButton("📱 Contato", callback_data='contato')],
            [InlineKeyboardButton("💻 Site", callback_data='site')],
            [InlineKeyboardButton("❌ Finalizar Atendimento", callback_data='finalizar_atendimento')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            f"Olá, {update.effective_user.first_name}! Em que posso te ajudar hoje?",
            reply_markup=reply_markup
        )
    
    elif query.data in FAQ:
        keyboard = [
            [InlineKeyboardButton("⬅️ Voltar ao Menu Principal", callback_data='menu_principal')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            f"{FAQ[query.data]}\n\n",
            reply_markup=reply_markup
        )
    
    return ESCOLHA