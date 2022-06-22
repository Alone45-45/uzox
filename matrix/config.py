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
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "AlONE_ASSISTANT")
BOT_IMAGE = getenv("BOT_IMAGE", "https://te.legra.ph/file/7e1e24c8cd10dcaf2b96b.jpg")
BOT_NAME = getenv("BOT_NAME", "Tom")
BOT_TOKEN = getenv("BOT_TOKEN", "5583584098:AAHkB6C2oca5NAWTnAIQShJVs7bFmP8kHWE")
BOT_USERNAME = getenv("BOT_USERNAME", "ALONEX_MUSIC_BOT")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
OWNER_NAME = getenv("OWNER_NAME", "UNK")
OWNER_USERNAME = getenv("OWNER_USERNAME", "TASTRON")
SOURCE_CODE = getenv("SOURCE_CODE", "https://t.me/TASTRON")
STRING_SESSION = getenv("STRING_SESSION", "AQCsFGCxvucR7V2a0OO0sjl7WYAgjoArZUcOW9eMtVMjr3Fm0GCAli3dk5dlY9IA4bLYm-Czj3yNS5j1oHiDeWPnvjzsLBWP6sAIDou7EqbvhfAYMMv90ybm1HxNl0f0RfRA811wtB0rmPEq0Cj9uiZtREhmoe2agwx8DL79lSbGxluoUDaQqFnP2wBEj3mPOKg_b6GMfNKhk8pgv0iqBxpurWaCai0KAXLS40avRECRS6X00MlEI5erpwsx544B78WDJFFfgXZw9-NPr1j0Tbk6rH9K0HLuckraPtDJzVjAxqX2arT3GAVBkgJdgcMBs5_2H0jySpfcNDmSWJTlD4wWAAAAAT78e5IA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5286943475").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/chatty_familia")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/TASTRON")


COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/UNK_LOGAN_0")
