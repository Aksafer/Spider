
import future
import asyncio
import os
import time
from urllib.parse import urlparse
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message
import wget
from pyrogram import filters
from pyrogram.types import Message
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
from AlinaXIQ import app
import asyncio
import os
import time
import wget
from urllib.parse import urlparse
from pyrogram import filters
from pyrogram.types import Message
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
from AlinaXIQ import app
from time import time
import asyncio
from AlinaXIQ.utils.extraction import extract_user
import asyncio
import os
import wget
from pyrogram import filters
from pyrogram.types import Message
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL

from AlinaXIQ import app
from AlinaXIQ.utils.extraction import extract_user

BANNED_USERS = []

@app.on_callback_query(filters.regex("downloadvideo") & ~filters.user(BANNED_USERS))
async def download_video(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    videoid = callback_data.split(None, 1)[1]
    user_id = CallbackQuery.from_user.id
    user_name = CallbackQuery.from_user.first_name
    chutiya = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    await CallbackQuery.answer("کەمێك چاوەڕێ بکە ئەزیزم . . .", show_alert=True)
    pablo = await client.send_message(CallbackQuery.message.chat.id, f"**● ꒐ {chutiya} دەگەڕێم بۆ ڤیدیۆ چاوەڕێ بکە 🧑🏻‍💻**")
    if not videoid:
        await pablo.edit(
            f"**● ꒐ {chutiya} گۆرانی نەدۆزرایەوە لە یوتوب دووبارە هەوڵدەوە**"
        )
        return

    search = SearchVideos(f"https://youtube.com/{videoid}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi.get("search_result", [])
    if not mio:
        await pablo.edit(f"**● ꒐ {chutiya} گۆرانی نەدۆزرایەوە لە یوتوب دووبارە هەوڵدەوە**")
        return

    mo = mio[0].get("link", "")
    thum = mio[0].get("title", "")
    fridayz = mio[0].get("id", "")
    thums = mio[0].get("channel", "")
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)

    except Exception as e:
        await pablo.edit(f"**● ꒐ شکستی هێنا\nهەڵە : **\n`{str(e)}`")
        return

    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"**🎸 ꒐ داگرترا : [{thum}]({mo})\n\n🧑🏻‍💻 ꒐ لەلایەن : {chutiya}**"
    try:
        await client.send_video(
            CallbackQuery.from_user.id,
            video=open(file_stark, "rb"),
            duration=int(ytdl_data["duration"]),
            file_name=str(ytdl_data["title"]),
            thumb=sedlyf,
            caption=capy,
            supports_streaming=True,
            progress_args=(
                pablo,
                f"**● ꒐ کەمێك چاوەڕێ بکە {chutiya}\n\n● ꒐ دایدەگرم لە یوتوبەوە**",
                file_stark,
            ),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"نوێکارییەکانی ئەلینا 🍻", url=f"https://t.me/MGIMT")]]))
      
        await client.send_message(CallbackQuery.message.chat.id, f"**● ꒐ ئەزیزم {chutiya}\n\n✅ ꒐ بە سەرکەوتوویی داگرترا\n● ꒐ ڤیدیۆم ناردە چاتی تایبەتی بۆت\n● ꒐ [ئێرە دابگرە](tg://openmessage?user_id={app.id}) 🎸**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"نوێکارییەکانی ئەلینا 🍻", url=f"https://t.me/MGIMT")]]))
        await pablo.delete()
        for files in (sedlyf, file_stark):
            if files and os.path.exists(files):
                os.remove(files)

    except Exception as e:
        await pablo.delete()
        return await client.send_message(CallbackQuery.message.chat.id, f"**● ꒐ {chutiya} بلۆکم لابدە تا بتوانم ڤیدیۆ دابگرم**", reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"🧑🏻‍💻 بلۆکم لابدە 🧑🏻‍💻", url=f"https://t.me/{app.username}?start=info_{videoid}")]]))




@app.on_callback_query(filters.regex("downloadaudio") & ~filters.user(BANNED_USERS))
async def download_audio(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    videoid = callback_data.split(None, 1)[1]
    user_id = CallbackQuery.from_user.id
    user_name = CallbackQuery.from_user.first_name
    chutiya = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    await CallbackQuery.answer("کەمێك چاوەڕێ بکە ئەزیزم . . .", show_alert=True)
    pablo = await client.send_message(CallbackQuery.message.chat.id, f"**● ꒐ {chutiya} دەگەڕێم بۆ گۆرانی چاوەڕێ بکە 🧑🏻‍💻**")
    if not videoid:
        await pablo.edit(
            f"**● ꒐ {chutiya} گۆرانی نەدۆزرایەوە لە یوتوب**"
        )
        return

    search = SearchVideos(f"https://youtube.com/{videoid}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi.get("search_result", [])
    if not mio:
        await pablo.edit(f"**● ꒐ {chutiya} گۆرانی نەدۆزرایەوە لە یوتوب دووبارە هەوڵدەوە**")
        return

    mo = mio[0].get("link", "")
    thum = mio[0].get("title", "")
    fridayz = mio[0].get("id", "")
    thums = mio[0].get("channel", "")
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "bestaudio/best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "outtmpl": "%(id)s.mp3",  # Output format changed to mp3
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)

    except Exception as e:
        await pablo.edit(f"**● ꒐ شکستی هێنا\nهەڵە : **\n`{str(e)}`")
        return

    file_stark = f"{ytdl_data['id']}.mp3"  # Adjusted file extension
    capy = f"**🎸 ꒐ داگرترا : [{thum}]({mo})\n\n🧑🏻‍💻 ꒐ لەلایەن : {chutiya}\n⏳ ꒐ ماوەکەی : {int(ytdl_data['duration']) // 60}:{int(ytdl_data['duration']) % 60}**"
    try:
        await client.send_audio(
            CallbackQuery.from_user.id,
            audio=open(file_stark, "rb"),
            title=str(ytdl_data["title"]),
            thumb=sedlyf,
            caption=capy,
            progress_args=(
                pablo,
                f"**● ꒐ کەمێك چاوەڕێ بکە {chutiya}\n\n● ꒐ دایدەگرم لە یوتوبەوە**",
                file_stark,
            ),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"نوێکارییەکانی ئەلینا 🍻", url=f"https://t.me/MGIMT")]]))
      
        await client.send_message(CallbackQuery.message.chat.id, f"**● ꒐ ئەزیزم {chutiya}\n\n✅ ꒐ بە سەرکەوتوویی داگرترا\n● ꒐ گۆرانیم ناردە چاتی تایبەتی بۆت\n● ꒐ [ئێرە دابگرە](tg://openmessage?user_id={app.id}) 🎸**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"نوێکارییەکانی ئەلینا 🍻", url=f"https://t.me/MGIMT")]]))
        await pablo.delete()
        for files in (sedlyf, file_stark):
            if files and os.path.exists(files):
                os.remove(files)

    except Exception as e:
        await pablo.delete()
        return await client.send_message(CallbackQuery.message.chat.id, f"**● ꒐ {chutiya} بلۆکم لابدە تا بتوانم گۆرانی دابگرم**", reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"🧑🏻‍💻 بلۆکم لابدە 🧑🏻‍💻", url=f"https://t.me/{app.username}?start=info_{videoid}")]]))
