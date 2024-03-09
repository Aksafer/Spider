from pyrogram import filters
from pyrogram.types import Message

from AlinaXIQ import app
from AlinaXIQ.core.call import Alina
from AlinaXIQ.utils.database import set_loop
from AlinaXIQ.utils.decorators import AdminRightsCheck
from AlinaXIQ.utils.inline import close_markup
from config import BANNED_USERS




# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
# ▒▒█▅▅▒▒▄██▒▒▄▇▇▇▇▇▇▄▒▒▄▇▇▇▇▇▇▄▒▒▄▇▇▇▇▇▇▄▒▒
# ▒▒▇▇▇▒▒▇▇▇▒▒▇▇▇▒▒▇▇▇▒▒▇▇▇▒▒██▉▒▒▇▇▇▒▒▇▇▇▒▒
# ▒▒▇▇▇▒▒▇▇▇▒▒▇▇▇▒▒▇▇▇▒▒▇▇▇▒▒██▉▒▒▇▇▇▒▒▇▇▇▒▒
# ▒▒▇▇▇▒▒▇▇▇▒▒▇▇▇▄▄▄▒▒▒▒▇▇▇▒▒▒▒▒▒▒▇▇▇▒▒▇▇▇▒▒
# ▒▒▇▇▇▒▒▇▇▇▒▒▇▇▇▀▀▀▒▒▒▒▇▇▇▒▀▇▇▇█▒▇▇▇▇▇▇██▒▒
# ▒▒▇▇▇▒▒▇▇▇▒▒▇▇▇▒▒▇▇▇▒▒▇▇▇▒▒▒▇▇▇▒▇▇▇▒▒▇▇▇▒▒
# ▒▒▇▇▇▒▒▇▇▇▒▒▇▇▇▒▒▇▇▇▒▒▇▇▇▒▒▒▇▇▇▒▇▇▇▒▒▇▇▇▒▒
# ▒▒▝▇▇▇▇▇█▘▒▒ ▇▇▇▇▇▇▘▒▒ ▇▇▇▇▇▇█▘▒ ██▘▒▒▝██▒▒
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
# 𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 
# (𝐂) 𝟐𝟎𝟐𝟒-𝟐𝟎𝟐𝟓 𝐛𝐲: @TOPVEGA
# 𝐆𝐫𝐞𝐞𝐭𝐢𝐧𝐠𝐬 𝐟𝐫𝐨𝐦 : 𝐕𝐞𝐆𝐚  

@app.on_message(
    filters.command(["end", "stop", "cend", "cstop"]) & filters.group & ~BANNED_USERS, group=717171)

@app.on_message(filters.command(["انها","ايقاف","انهاء"],"") & ~BANNED_USERS, group=999199890)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await Alina.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )


@app.on_message(filters.command(["end", "stop", "cend", "cstop"]) & filters.channel)
@app.on_message(filters.command(["انها","ايقاف","انهاء"],"") & filters.channel)
async def stop_musiccc(cli, message):
    if not len(message.command) == 1:
        return
    await Alina.stop_stream(message.chat.id)
    await set_loop(message.chat.id, 0)
    await message.reply_text(
        _["admin_5"].format(message.chat.title), reply_markup=close_markup(_)
    )
