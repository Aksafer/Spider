import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.enums import ParseMode, ChatMemberStatus
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AlinaXIQ import app, Telegram
import random



@app.on_message(
    command(["اغنيه"])
)
async def music(client: Client, message: Message):
    rl = random.randint(1, 29)
    url = f"https://t.me/FGRUL_3/{rl}"
    await client.send_voice(message.chat.id, url, caption="**[⧉• 𝙎𝙊𝙐𝙍𝘾𝙀 𝙀𝙍𝙊𝙍 - 🧑🏻‍💻🖤 اغنيه](t.me/YU_CQ)**\n\n**••┉┉┉┉┉••🝢••┉┉┉┉┉••**\n**¦  اغانيي➧♥**\n**@YU_CQ - قناة السورس**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    

@app.on_message(command(["صوره جامده","صوره"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(1,45)
    url = f"https://t.me/FGRUL_2/{rl}"
    await client.send_photo(message.chat.id,url,caption="**[⧉• 𝙎𝙊𝙐𝙍𝘾𝙀 𝙀𝙍𝙊𝙍 - 🧑🏻‍💻🖤 صور](t.me/YU_CQ)**\n**••┉┉┉┉┉••🝢••┉┉┉┉┉••**\n\n**¦ الصور ➧♥\n@YU_CQ - قناة السورس**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(
    command(["قراان"])
)
async def voice(client: Client, message: Message):
    rl = random.randint(1, 102)
    url = f"https://t.me/FGRUL_1/{rl}"
    await client.send_voice(message.chat.id, url, caption="**[⧉• 𝙎𝙊𝙐𝙍𝘾𝙀 𝙀𝙍𝙊𝙍 - 🧑🏻‍💻🖤 قران](t.me/YU_CQ)**\n**••┉┉┉┉┉••🝢••┉┉┉┉┉••**\n\n**¦ قران كريم➧♥️\n@YU_CQ - قناة السورس**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         message.from_user.first_name,
                                 url=f"https://t.me/{message.from_user.username}")
                ],
            ]
       )
  )

@app.on_message(command([f"فيديو", "v", "ڤ"])
)
async def video(client: Client, message: Message):
    rl = random.randint(5, 32)
    u = await client.get_messages("FGRUL_4",rl)
    if u.video:
     await client.send_video(message.chat.id, u.video.file_id, caption="**[⧉• 𝙎𝙊𝙐𝙍𝘾𝙀 𝙀𝙍𝙊𝙍 - 🧑🏻‍💻🖤 فيديوهات](t.me/YU_CQ)**\n**••┉┉┉┉┉••🝢••┉┉┉┉┉••**\n\n**¦ @YU_CQ - قناة السورس ♥•**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         message.from_user.first_name,
                                 url=f"https://t.me/{message.from_user.username}")
                ],
            ]
       )
       )

       

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
