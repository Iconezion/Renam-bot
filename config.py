# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21782653")

API_HASH = os.environ.get("API_HASH", "b9516b83f8c00a7b1157c785cfd7aa3e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", ""7144496753:AAFUeFX5j6bK3weVd1ioE36TcW2Bm8AWVko) 

FORCE_SUB = os.environ.get("FORCE_SUB", "Icon_Bot") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "icon_rename_bot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://iconezion:<password>@cluster037.dndwcx6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster037")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5443243023').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
