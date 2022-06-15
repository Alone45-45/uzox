import os
from pyrogram import client, filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton

UNK = Client(
  "SIMPLE_BOT",
  api_id = os.environ["API_ID"],
  api_hash = int(os.environ("API_HASH"),
    bot_token = os.environ("BOT_TOKEN")
  )

  START_TEXT = """
Hey I'm Your Advance Bot.
  """

  START_BUTTON = InlineKeyboardMarkup(
    [[
      InlineKeyboardButton('Owner',url = 'https://t.me/TASTRON'),
      InlineKeyboardButton = ('Group',url = 'https://t.me/Chatty_familia')
      InlineKeyboardButton('Help',callback_data = 'help'),
      InlineKeyboardButton('About',callback_data = 'about')
      InlineKeyboardButton('Close',callback_data = 'close')
    ]]
  )

  @UNK.on_callback_query()
  async def callback_handler(bot,update):
          if update.date == 'home':
              await update.message.edit_text(
              text = START_BUTTON.format(update.from_user.mention),
              reply_markup = START_BUTTON,
              disable_web_page_preview = True
  )
          elif update.date == 'about':
                await update.message.edit_text(
                text = START_BUTTON.format(update.from_user.mention),
                reply_markup = START_BUTTON,
                disable_web_page_preview = True
  )
          elif update.date == 'close':
                await update.message.edit_text(
                text = START_BUTTON.format(update.from_user.mention),
                reply_markup = START_BUTTON,
                disable_web_page_preview = True
  )
         else:=
               await update.message.delete()

@UNK.on.message(filters.private & filter.command(['start']))
async def start(bot,update):
  await update.reply_text(
    text=START_BUTTON.format(update,from_user.mention),
    disable_web_page_preview=True
    reply_markup=START_BUTTON
  )
  
UNK.run()