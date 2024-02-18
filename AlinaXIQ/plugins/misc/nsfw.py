import os
import asyncio
import requests
import urllib.request
from pyrogram import Client, filters
from AlinaXIQ import app

# Temporary download directory
TEMP_DOWNLOAD_DIRECTORY = "temp/"

# Ensure the temporary directory exists
os.makedirs(TEMP_DOWNLOAD_DIRECTORY, exist_ok=True)

# Define the command handler
@app.on_message(filters.command("get_nsfw", prefixes="/"))
async def get_nsfw_command(client, message):
    pic_loc = os.path.join(TEMP_DOWNLOAD_DIRECTORY, "bobs.jpg")
    a = await message.reply_text("**Mencari Gambar Bugil**")
    await asyncio.sleep(0.5)
    await a.edit("`Mengirim foto bugil...`")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await client.send_photo(message.chat.id, photo=pic_loc, caption="**Sange boleh, Goblok jangan**")
    os.remove(pic_loc)
