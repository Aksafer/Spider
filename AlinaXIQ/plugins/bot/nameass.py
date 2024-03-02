from pyrogram import filters, Client
from AlinaXIQ import app
import asyncio
from AlinaXIQ.misc import SUDOERS
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AlinaXIQ.core.call import Alina
from AlinaXIQ.utils.database import *
from pytgcalls.exceptions import NoActiveGroupCall, TelegramServerError

@app.on_message(filters.regex(["گۆڕینی ناوی یاریدەدەر"،"/nameassistant"]) SUDOERS)
async def tom_name(client, message):
    assistant = await group_assistant(Alina, message.chat.id)
    await message.reply("**🧑🏻‍💻┋ ناوی نوێی یاریدەدەر بنێرە**")
    try:
        new_name = await client.ask(message.chat.id, "**🧑🏻‍💻┋ ناوی نوێی یاریدەدەر بنووسە**")
        await assistant.update_profile(first_name=new_name)
        await message.reply(f"**🎻┋ ناوی یاریدەدەر گۆڕا بۆ {new_name} **")
    except Exception as e:
        await message.reply("**🧑🏻‍💻┋ هەڵە ڕویدا لە کاتی گؤرینی ناو**")
