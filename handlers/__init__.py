import re
import sys
import time
from config import (API_ID, API_HASH, BOT_TOKEN)

from pyrogram import Client

StartTime = time.time()

app = Client(
    "𝐎𝐬𝐦𝐚𝐧𝐢 𝐁𝐨𝐭𝐬",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)

