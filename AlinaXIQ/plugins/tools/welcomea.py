from AlinaXIQ import app
from pyrogram.errors import RPCError
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
from os import environ
import random
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, time, aiohttp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from asyncio import sleep
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode
from logging import getLogger
from AlinaXIQ.utils.alina_ban import admin_filter
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from AlinaXIQ import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)







LOGGER = getLogger(__name__)

class WelDatabase:
    def __init__(self):
        self.data = {}

    async def find_one(self, chat_id):
        return chat_id in self.data

    async def add_wlcm(self, chat_id):
        if chat_id not in self.data:
            self.data[chat_id] = {"state": "on"}  # Default state is "on"

    async def rm_wlcm(self, chat_id):
        if chat_id in self.data:
            del self.data[chat_id]

wlcm = WelDatabase()

class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None



@app.on_message(filters.command(["welcome", "wel"]) & ~filters.private)
async def auto_state(_, message):
    usage = "**بەکارهێنان:**\n⦿/wel [on|off]\n"
    if len(message.command) == 1:
        return await message.reply_text(usage)
    chat_id = message.chat.id
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
        A = await wlcm.find_one(chat_id)
        state = message.text.split(None, 1)[1].strip().lower()
        if state == "off":
            if A:
                await message.reply_text("**بەخێرهاتن پێشتر لەکارخراوە**")
            else:
                await wlcm.add_wlcm(chat_id)
                await message.reply_text(f"**بەخێرهاتن لەکارخرا لە {message.chat.title}**")
        elif state == "on":
            if not A:
                await message.reply_text("**بەخێرهاتن پێشتر چالاککراوە**")
            else:
                await wlcm.rm_wlcm(chat_id)
                await message.reply_text(f"**بەخێرهاتن چالاککرا لە {message.chat.title}**")
        else:
            await message.reply_text(usage)
    else:
        await message.reply("**چالاکردنی فەرمانی بەخێرهاتن تەنیا بۆ ئەدمینەکان**")



@app.on_chat_member_updated(filters.group, group=-3)
async def greet_new_member(_, member: ChatMemberUpdated):
    try:
        
        chat_id = member.chat.id
        A = await wlcm.find_one(chat_id)
        if A:
            return

        user = member.new_chat_member.user if member.new_chat_member else member.from_user
        
        # Add the modified condition here
        if member.new_chat_member and not member.old_chat_member and member.new_chat_member.status != "kicked":
            welcome_text = f"""**◗⋮◖ بەخێربێی ئەزیزم {user.mention}\n بۆ گرووپی {message.chat.title}**"""
            await app.send_message(chat_id, text=welcome_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"نوێکارییەکانی ئەلینا 🍻", url=f"https://t.me/MGIMT")]]))
    except Exception as e:
       LOGGER.error(e)
