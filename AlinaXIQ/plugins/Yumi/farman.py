import asyncio

import os
import time
import requests
from config import BOT_NAME
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AlinaXIQ import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AlinaXIQ import app
from random import  choice, randint

@app.on_message(
    command(["/help"])
 )
async def mmmezat(client, message):
        await message.reply_text(f"""⧉ 𝙎𝙊𝙐𝙍𝘾𝙀 𝙀𝙍𝙊𝙍 - أمرك🧑🏻 💻🖤\n••┉┉┉┉┉┉••🝢••┉┉┉┉┉┉••\n\nمرحبًا {message.from_user.mention} للقسم الختامي و افتح الأمر {MUSIC_BOT_NAME}\n\n
 فتح + الأمر 👾✅

 معرف | صورة

 الرد | ملصقات

      ذكر

⩹⊶⊷⌯⧉• 𝙎𝙊𝙐𝙍𝘾𝙀 𝙀𝙍𝙊𝙍 •⧉⊶⊷⋗

 إغلاق + أمر 👾❎

 معرف | صورة

 الرد | ملصقات

      ذكر

مثال: فتح هوية أو إغلاق هوية♥🧩

مثال: فتح أو إغلاق الذكر♥🧩

@Y_D_ll - 🖤👾أفضل بوت أغنية وحماية واستجابة
**"""،


        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⧉• 𝙎𝙊𝙐𝙍𝘾𝙀 𝙀𝙍𝙊𝙍 ", url=f"https://t.me/YU_CQ"),                        
                 ],[
                InlineKeyboardButton(
                        "مبرمج⚡", url=f"https://t.me/Y_D_ll"),
               ],
          ]
        ),
    )
