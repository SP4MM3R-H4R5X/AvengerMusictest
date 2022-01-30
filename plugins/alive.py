import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
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
    await message.reply_video(
        photo=f"https://telegra.ph/file/3c01ff0605509dc12fff3.mp4",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ : [ᴍᴜᴋᴇꜱʜ](https://t.me/mkspali)
┗━━━━━━━━━━━━━━━━━┛
💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ [ᴀᴠᴇɴɢᴇʀ ᴏᴡɴᴇʀ](https://t.me/mkspali)
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/BotsClubOfficial"),
                    InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/BotsClubDiscussion"),
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_video(
        photo=f"https://telegra.ph/file/d5d6c6d8196872b6cf8a0.mp4",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/BotsClubOfficial"),
                    InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/BotsClubDiscussion"),
                ]
            ]
        ),
    )
