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
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "Nobita_Assistant0")
BOT_IMAGE = getenv("BOT_IMAGE", "https://te.legra.ph/file/7e1e24c8cd10dcaf2b96b.jpg")
BOT_NAME = getenv("BOT_NAME", "Tom")
BOT_TOKEN = getenv("BOT_TOKEN", "5402735634:AAGL6NYAMiEep3ip5d0OPQ8yHfid5tRxEPw")
BOT_USERNAME = getenv("BOT_USERNAME", "Test91817_bot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
OWNER_NAME = getenv("OWNER_NAME", "UNK")
OWNER_USERNAME = getenv("OWNER_USERNAME", "TASTRON")
SOURCE_CODE = getenv("SOURCE_CODE", "https://t.me/TASTRON")
STRING_SESSION = getenv("STRING_SESSION", "BQDFRFS3vHKSU1ye4tjb2L_bhS3_nY39il9j0rp8x7j-90MF9NKVN0P2StF377VFHE-gJKm9FsJ0g5a3pgZQi1MfFSJRNJoemll1HITBV8YWcG0dAT8Ut33hVXAm5iTqonUSNorqBSrtoAypV4QenmX5OUHtnKp_LzWyityjdUgQnmmJKfACuKu1c-vP-wevQ_ticfrUfKK6TUwVWa3G5VpscasM5i51or7EwCshcOxbcU83bmUjIwIVdiDPM7NGG5CzQTu5aufLMKugT4Iq120GouKuR3oiywcVE6SvWQUluCurNOwSZvmj9UAesi_4J6UedQAZDfmbQTr-enMI8lj6AAAAAUTDWqkA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5286943475").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/chatty_familia")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/TASTRON")


COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/UNK_LOGAN_0")
