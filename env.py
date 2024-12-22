import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "22768571").strip()
API_HASH = os.getenv("API_HASH", "7d92204d9b502be216843739f70ded0e").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "7604555634:AAGWMfCKmcumls1Pr0y1QyqTDrUPKcqyHns").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://meyitzadee:Mytbot47@mytbot.a6b81.mongodb.net/?retryWrites=true&w=majority&appName=MytBot").strip() # Not a necessary variable anymore but you can add to get stats
MUST_JOIN = os.getenv("MUST_JOIN", "MytSohbet")

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")
'''
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit
'''

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
