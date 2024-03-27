import future

import asyncio
import os
import time
from urllib.parse import urlparse
from pyrogram.types import (InlineKeyboardButton, CallbackQuery,
                            InlineKeyboardMarkup, Message)
import wget
from pyrogram import filters
from pyrogram.types import Message
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
from AlinaXIQ import YouTube
from youtubesearchpython import VideosSearch
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

@app.on_callback_query(filters.regex("download_video") & ~filters.user(BANNED_USERS))
async def download_video(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    videoid = callback_data.split("_")[0]  # Extract video ID from callback data
    user_id = CallbackQuery.from_user.id
    user_name = CallbackQuery.from_user.mentoin
    chutiya = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    pablo = await client.send_message(CallbackQuery.message.chat.id, f"**● ꒐ دەگەڕێم بۆ {videoid} کەمێك چاوەڕێ بکە 🧑🏻‍💻**")
    if not videoid:
        await pablo.edit(
            "**● ꒐ گۆرانی نەدۆزرایەوە لە یوتوب\n● ꒐ ناوی گۆرانی هەڵە نووسراوە**"
        )
        return
    # Rest of the function remains unchanged...


    search = SearchVideos(f"https://youtube.com/{videoid}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi.get("search_result", [])
    if not mio:
        await pablo.edit("**● ꒐ گۆرانی نەدۆزرایەوە لە یوتوب 🧑🏻‍💻**")
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
        await pablo.edit(f"**● ꒐ شکستی هێنا\nهەڵە : **\n `{str(e)}`")
        return

    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"**● ꒐ لەلایەن : {app.mention} **"
    await client.send_video(
        CallbackQuery.message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,
        progress_args=(
            pablo,
            f"**● ꒐ کەمێك چاوەڕێ بکە\n\n● ꒐ دادەبەزێت** `{videoid}` **لە یوتوبەوە 🧑🏻‍💻**",
            file_stark,
        ),
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)


@app.on_callback_query(filters.regex("download_audio") & ~filters.user(BANNED_USERS))
async def download_audio(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    videoid = callback_data.split("_")[1]  # Extract video ID from callback data
    user_id = CallbackQuery.from_user.id
    user_name = CallbackQuery.from_user.mentoin
    chutiya = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    print(videoid)
    m = await client.send_message(CallbackQuery.message.chat.id, f"**● ꒐ دەگەڕێم کەمێك چاوەڕێ بکە 🧑🏻‍💻**")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YouTube.track(f"https://youtube.com/{videoid}", max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

        # Add these lines to define views and channel_name
        views = results[0]["views"]
        channel_name = results[0]["channel"]

    except Exception as e:
        await m.edit("**● ꒐ گۆرانی نەدۆزرایەوە لە یوتوب\n● ꒐ ناوی گۆرانی هەڵە نووسراوە**")
        print(str(e))
        return
    await m.edit("**📥 داونڵۆد . .**")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        await m.edit("**📤 دایدەگرم . .**")

        await message.reply_audio(
            audio_file,
            thumb=thumb_name,
            title=title,
            caption=f"**● ꒐ لەلایەن : {app.mention} **",
            duration=dur
        )
        await m.delete()
    except Exception as e:
        await m.edit("**● ꒐ شکستی هێنا**")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
