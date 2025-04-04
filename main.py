import logging
from config import BOT_TOKEN
from database.db_manager import db_manager
from utils.constants import (
    FEEDBACK, CONTATO_NOME, CONTATO_EMAIL, CONTATO_MENSAGEM
)
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, 
    filters, CallbackQueryHandler, ConversationHandler
)

from handlers.menu import menu_callback
from handlers.feedback import iniciar_feedback, processar_feedback
from handlers.message import processar_mensagem
from handlers.contact import (
    iniciar_contato, processar_contato_nome, 
    processar_contato_email, processar_contato_mensagem
)
from handlers.command import (
    start, ajuda, produtos, horario, site, sobre, endereco, finalizar_atendimento
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    db_manager.init_db()
    
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    feedback_conv = ConversationHandler(
        entry_points=[CommandHandler("feedback", iniciar_feedback)],
        states={
            FEEDBACK: [MessageHandler(filters.TEXT & ~filters.COMMAND, processar_feedback)]
        },
        fallbacks=[CommandHandler("cancel", start)]
    )
    
    contato_conv = ConversationHandler(
        entry_points=[CommandHandler("contato", iniciar_contato)],
        states={
            CONTATO_NOME: [MessageHandler(filters.TEXT & ~filters.COMMAND, processar_contato_nome)],
            CONTATO_EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, processar_contato_email)],
            CONTATO_MENSAGEM: [MessageHandler(filters.TEXT & ~filters.COMMAND, processar_contato_mensagem)]
        },
        fallbacks=[CommandHandler("cancel", start)]
    )
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ajuda", ajuda))
    application.add_handler(CommandHandler("horario", horario))
    application.add_handler(CommandHandler("site", site))
    application.add_handler(CommandHandler("sobre", sobre))
    application.add_handler(CommandHandler("endereco", endereco))
    application.add_handler(CommandHandler("produtos", produtos))
    application.add_handler(CommandHandler("finalizar", finalizar_atendimento))
    
    application.add_handler(feedback_conv)
    application.add_handler(contato_conv)
    
    application.add_handler(CallbackQueryHandler(menu_callback))
    
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, processar_mensagem))
    
    print("Bot iniciado!")
    application.run_polling()

if __name__ == '__main__':
    main()