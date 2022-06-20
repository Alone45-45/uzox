import os
import aiohttp
from os import getenv
from dotenv import load_dotenv


load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_HASH = getenv("API_HASH", "c426d9f7087744afdafc961a620b6338")
API_ID = int(getenv("API_ID", "9683694"))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ᴀʟᴏɴᴇ ᴀꜱꜱɪꜱᴛᴀɴᴛ")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "AlONE_ASSISTANT1")
BOT_IMAGE = getenv("BOT_IMAGE", "https://te.legra.ph/file/7e1e24c8cd10dcaf2b96b.jpg")
BOT_NAME = getenv("BOT_NAME", "Tom")
BOT_TOKEN = getenv("BOT_TOKEN", "5583584098:AAFLkWCg_S4wAo7X2wKy1TmpVGPlNau1wrY")
BOT_USERNAME = getenv("BOT_USERNAME", "ALONEX_MUSIC_BOT")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
OWNER_NAME = getenv("OWNER_NAME", "UNK")
OWNER_USERNAME = getenv("OWNER_USERNAME", "TASTRON")
SOURCE_CODE = getenv("SOURCE_CODE", "https://t.me/TASTRON")
STRING_SESSION = getenv("STRING_SESSION", "AQAOfJ_PsRyjJlOPR66_-oOXvd1YLrVgTjpLFucNIex7M4uzcOkRWwEdTllGdty4YweDySana8dOzPJ7aGTHuTDq5fngPCrTVioF7tux5mDOxQtbLd8xqPmav8YUSU9cI2qoywYSlBLHL7SU_Gcg6X--jFzr_O77hNADTGTs2DbE0wqkgLsSZog4SB4kWahakimqvnAIfOXmtp6TG3YPswOTrHHkcevhglBUU1BoGIjqA03jXPQob9LRydEu6vByJARvLcAuNaL7H8T3U27BKu6bApf7w7d7prRJA0yyB6-HTPIjHkmZONUUlCpyQduRp-jTAiefulyR0mUMqouJ1SYOAAAAAUECmfsA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5286943475").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/chatty_familia")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/TASTRON")


COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/UNK_LOGAN_0")
