import asyncio
from time import time
from datetime import datetime
from matrix.config import BOT_IMAGE, BOT_USERNAME, OWNER_USERNAME, UPDATES_CHANNEL, SUPPORT_GROUP, SOURCE_CODE
from matrix.maintain.filters import command
from matrix.maintain.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""**═════════════════════════
⚙️ ɪ'ᴍ ʏᴏᴜʀ ᴀᴅᴠᴀɴᴄᴇ ʙᴏᴛ ɴᴏ ʟᴀɢ ɢʀᴏᴜᴘ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ
┏═════════════════┓
┣★  ᴏᴡɴᴇʀ ➪  » [ᴛᴏᴜᴄʜ ᴍᴇ ʙᴜʙᴜ](https://t.me/{OWNER_USERNAME})
┣★ ʜᴇᴀʀᴛ ꜱᴏᴜʟ  ➪ » [ᴛᴏᴜᴄʜ ᴍᴇ ʙᴜʙᴜ]({UPDATES_CHANNEL})
┣★ ᴄʟᴜꜱᴛᴇʀ ➪ » [ᴛᴏᴜᴄʜ ᴍᴇ ʙᴜʙᴜ]({SUPPORT_GROUP})
┗═════════════════┛

☺️ ᴋᴇᴇᴘ ꜱᴍɪʟᴇ ᴏɴ ʏᴏᴜʀ ꜰᴀᴄᴇ ☺️
════════════════════════**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 🥵 𝐀𝐃𝐃 𝐌𝐄 𝐇𝐎𝐍𝐄𝐘 🥵 ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", f"start@{BOT_USERNAME}", "/alive", ".alive", "#aditya"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🙈ᴍᴇ ᴀᴀ ɢᴀɪ ʙᴀʙʏ🙈", url=f"{SUPPORT_GROUP}")
                ]
            ]
        ),
    )


