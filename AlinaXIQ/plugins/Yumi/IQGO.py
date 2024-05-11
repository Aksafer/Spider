import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.enums import ParseMode, ChatMemberStatus
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AlinaXIQ import app, Telegram
import random




bio = []

@app.on_message(
    command(["بايو"])
    & filters.group
)
async def idjjdd(client, message:Message):
    if message.chat.id in bio:
      return
    usr = await client.get_chat(message.from_user.id)
    await message.reply_text(f"**هذه هي سيرتك الذاتية\n│ \n└ʙʏ: {usr.bio}**")
