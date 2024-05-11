import asyncio

import os
import time
import requests
from config import USER_OWNER, OWNER_ID, SUPPORT_CHANNEL, OWNER_CHANNEL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AlinaXIQ import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AlinaXIQ import app
from random import  choice, randint
from asyncio import gather
from pyrogram.errors import FloodWait
from pyrogram.enums import ParseMode, ChatMemberStatus


                
@app.on_message(
    command(["/source", "سورس" ,"السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/b4ace5c5aec2901efed59.jpg",
        caption=f"""**[⧉• 𝙎𝙊𝙐𝙍𝘾𝙀 𝙀𝙍𝙊𝙍 - 🧑🏻‍💻🖤 المطور](t.me/YU_CQ)**\n••┉┉┉┉┉••🝢••┉┉┉┉┉••\n**أهلا بك عزيزي{message.from_user.mention} في قسم مطورين السورس**\n**اتواصل بنا لو في اي مشاكل عندك من خلال الازرار♥•**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒مـبـرمـج الـسـورس", url=f"https://t.me/Y_D_ll"), 
                 ],[
                    
                
                    InlineKeyboardButton(
                        "الـــســـوبـــر", url=f"https://t.me/AC_LU"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "𝙎𝙊𝙐𝙍𝘾𝙀 𝙀𝙍𝙊𝙍", url=f"https://t.me/YU_CQ"),
                
        ],[
                    
                
                    InlineKeyboardButton(
                        "جـروب الـدعـم", url=f"https://t.me/YR_HC"),
                ],

            ]

        ),

    )


@app.on_message(command(["bot", "بوت", "بوت"]) & filters.group)
async def iqbot(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/426283f861812c31153d1.jpg",
        caption=f"""**• أفضل بوت ميوزك**\n\n**• البوت يعمل بي شكل رائع\n\n**• 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 -› [مـطـور الـسـورس](t.me/Y_D_ll)**\n**• 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 -› [قـنـاة الـسـورس](t.me/YU_CQ)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙎𝙊𝙐𝙍𝘾𝙀 𝙀𝙍𝙊𝙍", url=f"https://t.me/YU_CQ"),
                ], [
                InlineKeyboardButton(
                    "أضفني إلى مجموعتك 🎻", url=f"https://t.me/IQMCBOT?startgroup=true"),
            ],
            ]
        ),
    )
                

@app.on_message(
    command(["مطور السورس"])
 
)
async def yas(client, message):
    
    usr = await client.get_chat("Y_D_ll")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**[⧉• 𝙎𝙊𝙐𝙍𝘾𝙀 𝙀𝙍𝙊𝙍 - مطور 🧑🏻‍💻](t.me/YU_CQ)\nمعرفة مطور السورس\n↜︙𝐍𝐀𝐌𝐄 ↬:{name}\n↜︙𝐔𝐒𝐄𝐑 ↬ :@{usr.username}\n↜︙𝐈𝐃 ↬ :`{usr.id}`\n↜︙𝐁𝐈𝐎 ↬: {usr.bio}**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
   command(["مبرمج السورس"])
   
)
async def yas(client, message):
    usr = await client.get_chat("Y_D_ll")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**[⧉• 𝙎𝙊𝙐𝙍𝘾𝙀 𝙀𝙍𝙊𝙍 - 🧑🏻‍💻🖤 مبرمج](t.me/YU_CQ)\nمعرفة مبرمج السورس\n↜︙𝐍𝐀𝐌𝐄 ↬:{name}\n↜︙𝐔𝐒𝐄𝐑 ↬ :@{usr.username}\n↜︙𝐈𝐃 ↬ :`{usr.id}`\n↜︙𝐁𝐈𝐎 ↬: {usr.bio}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],  [
                    InlineKeyboardButton(
                        "🝢 للتوصل 🝢", url=f"https://t.me/{usr.username}"),                        
                 ],
            ]
        ),
    )


    
@app.on_message(command(["المالك","مالك الجروب","owner"]) & filters.group)
async def gak_owne(client: Client, message: Message):
      if len(message.command) >= 2:
         return 
      else:
            chat_id = message.chat.id
          
            async for member in client.get_chat_members(chat_id):
               if member.status == ChatMemberStatus.OWNER:
                 id = member.user.id
                 key = InlineKeyboardMarkup([[InlineKeyboardButton(member.user.first_name, user_id=id)]])
                 m = await client.get_chat(id)
                 if m.photo:
                       photo = await app.download_media(m.photo.big_file_id)
                       return await message.reply_photo(photo, caption=f"**✧ معلومات مالك المجموعة \n\n ✧ ¦ اسـم ← {m.first_name} \n ✧ ¦ يوزر ← @{m.username} \n ✧ ¦ بايو ← {m.bio}**",reply_markup=key)
                 else:
                    return await message.reply("•" + member.user.mention)
                       
                    
                    
@app.on_message(command(["جروب", "group"]) & filters.group)
async def ginnj(client: Client, message: Message):
    chat_idd = message.chat.id
    chat_name = message.chat.title
    chat_username = f"@{message.chat.username}"
    photo = await client.download_media(message.chat.photo.big_file_id)
    await message.reply_photo(photo=photo, caption=f"""**🦩 ¦ ꪀᥲ️ꪔᥱ » {chat_name}\n🐉 ¦ Ꭵժ ᘜᖇ᥆υρ »  -{chat_idd}\n🐊 ¦ ᥣᎥꪀk » {chat_username}**""",     
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        chat_name, url=f"https://t.me/{message.chat.username}")
                ],
            ]
        ),
    )
    

@app.on_message(command(["ملصق","تحويل الي صوره"]))
async def sticker_image(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("**ملصقات الرد**")
    if not reply.sticker:
        return await message.reply("**ملصقات الرد**")
    m = await message.reply("**جاري التحميل . .**")
    f = await reply.download(f"{reply.sticker.file_unique_id}.png")
    await gather(*[message.reply_photo(f),message.reply_document(f)])
    await m.delete()
    os.remove(f)
      
   
@app.on_message(command(["اسمي","نيمي"]) & filters.group )
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""•⎆┊** اســــمــــك 🔥♥**»»  {message.from_user.mention()}""") 
