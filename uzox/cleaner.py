import os
from pyrogram import Client, filters
from pyrogram.types import Message
from matrix.maintain.filters import command, other_filters
from matrix.maintain.decorators import sudo_users_only, errors

downloads = os.path.realpath("downloads")
raw_files = os.path.realpath("raw_files")

@Client.on_message(command(["rmd", "clear"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("☑️ **ᴅᴇʟᴇᴛᴇ ʜᴏ ɢʏᴀ ᴊᴀᴀɴᴜ ...**")
    else:
        await message.reply_text("✖️ **ʙᴀʙʏ ᴀʟʟ ꜰɪʟᴇ ᴄʟᴇᴀʀᴇᴅ...**")

        
@Client.on_message(command(["rmr", "clean"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw_files)
    if ls_dir:
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("☑️ **ʀᴀᴡ ꜰɪʟᴇ ᴅᴇʟᴇᴛᴇ ʜᴏ ɢᴀɪ ᴊᴀᴀɴᴜ ...**")
    else:
        await message.reply_text("✖️ **ʙᴀʙʏ ᴀʟʟ ʀᴀᴡ ꜰɪʟᴇ ᴄʟᴇᴀʀᴇᴅ ...**")


@Client.on_message(command(["cleanup"]) & ~filters.edited)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("☑️ **ᴀʟʟ ᴛʜᴜᴍʙɴᴀɪʟ ᴄʟᴇᴀʀ ᴊᴀᴀɴᴜ ...**")
    else:
        await message.reply_text("☑️ **ʙᴀʙʏ ᴀʟʟ ᴊᴜɴᴋꜱ ᴄʟᴇᴀʀᴇᴅ ...**")
