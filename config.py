import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('TOKEN_BOT_TELEGRAM')

DB_URL = os.getenv('DATABASE_URL')