# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()

# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "26180065"))
API_HASH = os.environ.get("API_HASH", "0a6358307acf8d0d2bf98b6827e0f5c7")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6992264465:AAFLUE_QV50Ly9OBpp3IGAo_mkMyfl984-4")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS", "6072149828").split(",") if i.strip()] 
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "shortener")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://errorsmonster:S.Aruna1155182089@shortener.woficdt.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "6072149828")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002115739348")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "MrAK_LinkZz") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://graph.org/file/8cd764fbdf3ccd34abe22.jpg') # image when someone hit /start
LINK_BYPASS = "False"
