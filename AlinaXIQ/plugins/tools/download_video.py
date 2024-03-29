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
from VIPMUSIC import app
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

from AlinaXIQ.utils.extraction import extract_user


import asyncio
import os
import requests
import wget
from pyrogram import filters
from pyrogram.types import Message
from yt_dlp import YoutubeDL

from AlinaXIQ import app
from AlinaXIQ.utils.extraction import extract_user

BANNED_USERS = []

@app.on_callback_query(filters.regex("downloadvideo") & ~filters.user(BANNED_USERS))
async def downloadvideo(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    videoid = callback_data.split()[1]  # Extract video ID from callback data
    pablo = await client.send_message(CallbackQuery.message.chat.id, f"**● ꒐ دەگەڕێم بۆ {videoid}, کەمێك چاوەڕێ بکە 🧑🏻‍💻**")
    
    if not videoid:
        await pablo.edit("**● ꒐ گۆرانی نەدۆزرایەوە لە یوتوب\n● ꒐ ناوی گۆرانی هەڵە نووسراوە**")
        return
    
    search = YouTube(f"https://youtube.com/{videoid}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi.get("search_result", [])
    if not mio:
        await pablo.edit("**● ꒐ گۆرانی نەدۆزرایەوە لە یوتوب 🧑🏻‍💻**")
        return

    mo = search.link
    thum = search.title
    fridayz = search.id
    thums = search.channel
    kekme = f"https://img.youtube.com/vi/{fridayz}/maxresdefault.jpg"
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

@app.on_callback_query(filters.regex("downloadaudio") & ~filters.user(BANNED_USERS))
async def downloadaudio(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    videoid = callback_data.split()[1]  # Extract video ID from callback data
    m = await client.send_message(CallbackQuery.message.chat.id, f"**● ꒐ دەگەڕێم کەمێك چاوەڕێ بکە 🧑🏻‍💻 {videoid}**")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YouTube(f"https://youtube.com/{videoid}")
        link = f"https://youtube.com{videoid}"
        title = results.title
        thumbnail = results.thumbnails
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

        # Add these lines to define views and channel_name
        views = results.views
        channel_name = results.channel

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

        await client.send_audio(
            CallbackQuery.message.chat.id,
            audio=open(audio_file, "rb"),
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
