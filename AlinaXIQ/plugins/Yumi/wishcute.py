from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
import requests
from AlinaXIQ import app 

SUPPORT_CHAT = "MGIMT"

@app.on_message(filters.command(["wish","حەز","هیوا","خۆزگە"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def wish(_, m):
    if len(m.command) < 2:
        await m.reply("**لەگەڵ فەرمانەکە خۆزگە یان حەزەکانت بنووسە 🥺🫶🏻**")
        return 

    api = requests.get("https://nekos.best/api/v2/happy").json()
    url = api["results"][0]['url']
    text = m.text.split(None, 1)[1]
    wish_count = random.randint(1, 100)
    wish = f"**🍓 سڵاو {m.from_user.first_name}!**\n"
    wish += f"**🍓 حەزی تۆ: {text} **\n\n"
    wish += f"**🍓 ڕێژەی ڕوودانی: {wish_count}% **"
    
    await app.send_animation(
        chat_id=m.chat.id,
        animation=url,
        caption=wish,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("نوێکارییەکانی ئەلینا 🍻", url=f"https://t.me/{SUPPORT_CHAT}")]])
    )
            
    
BUTTON = [[InlineKeyboardButton("نوێکارییەکانی ئەلینا 🍻", url=f"https://t.me/{SUPPORT_CHAT}")]]
CUTIE = "https://graph.org/file/ff4ee737b9daeb83fa0ec.mp4"

@app.on_message(filters.command(["cute","کیوت","كیوت","قشت","قشتی"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def cute(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CUTE = f"**🍓 {mention}\nڕێژەی قشتیت {mm}% 🥺🫶🏻**"

    await app.send_file(
        chat_id=message.chat.id,
        video=CUTIE,
        caption=CUTE,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
    )
    
help_text = """
» ᴡʜᴀᴛ ɪꜱ ᴛʜɪꜱ (ᴡɪꜱʜ):
ʏᴏᴜ ʜᴀᴠɪɴɢ ᴀɴʏ ᴋɪɴᴅ ᴏꜰ 
(ᴡɪꜱʜᴇꜱ) ʏᴏᴜ ᴄᴀɴ ᴜꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ᴛᴏ ʜᴏᴡ ᴘᴏꜱꜱɪʙʟᴇ ᴛᴏ ʏᴏᴜʀ ᴡɪꜱʜ!
ᴇxᴀᴍᴘʟᴇ:» /wish : ɪ ᴡᴀɴᴛ ᴄʟᴀꜱꜱ ᴛᴏᴘᴘᴇʀ 
» /wish : ɪ ᴡᴀɴᴛ ᴀ ɴᴇᴡ ɪᴘʜᴏɴᴇ 
» /cute : ʜᴏᴡ ᴍᴜᴄʜ ɪ ᴀᴍ ᴄᴜᴛᴇ 
"""
