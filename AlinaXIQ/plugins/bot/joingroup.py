from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
from pyrogram.enums import ChatType
from pyrogram.errors import UserNotParticipant
from AlinaXIQ import app

channel = "EHS4SS"


async def subscription(_, __: Client, message: Message):
    try:
        await app.get_chat_member(channel, sender)
    except UserNotParticipant:
        return False
    return True


subscribed = filters.create(subscription)


@app.on_message(~subscribed)
async def checker(_, __: Client, message: Message):
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]: await message.delete()
    sender = await app.get_chat_member(message.chat.id, message.from_user.id)
    user = message.from_user.mentoin
    markup = Markup([
        [Button("𝗦𝗼𝘂𝗿𝗰𝗲 𝗔𝗹𝗶𝗻𝗮 🎻", url=f"https://t.me/{channel}")]
    ])
    await message.reply(
        f"**🧑🏻‍💻┋ ببورە ئەزیزم {user}؛\n🎻┋ پێویستە سەرەتا جۆینی کەناڵی بۆت بکەیت؛\n✅┋ کەناڵی بۆت : {channel}**",
        reply_markup=markup
    )
