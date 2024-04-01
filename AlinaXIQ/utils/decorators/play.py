import asyncio

from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AlinaXIQ import YouTube, app
from AlinaXIQ.misc import SUDOERS
from AlinaXIQ.utils.database import (
    get_assistant,
    get_cmode,
    get_lang,
    get_playmode,
    get_playtype,
    is_active_chat,
    is_maintenance,
)
from AlinaXIQ.utils.inline import botplaylist_markup
from config import PLAYLIST_IMG_URL, SUPPORT_CHAT, adminlist
from strings import get_string

links = {}


def PlayWrapper(command):
    async def wrapper(client, message):
        language = await get_lang(message.chat.id)
        _ = get_string(language)
    
        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    text=f"{app.mention} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ, ᴠɪsɪᴛ <a href={SUPPORT_CHAT}>sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ</a> ғᴏʀ ᴋɴᴏᴡɪɴɢ ᴛʜᴇ ʀᴇᴀsᴏɴ.",
                    disable_web_page_preview=True,
                )

        try:
            await message.delete()
        except:
            pass

        audio_telegram = (
            (message.reply_to_message.audio or message.reply_to_message.voice)
            if message.reply_to_message
            else None
        )
        video_telegram = (
            (message.reply_to_message.video or message.reply_to_message.document)
            if message.reply_to_message
            else None
        )
        url = await YouTube.url(message)
        if audio_telegram is None and video_telegram is None and url is None:
            if len(message.command) < 2:
                if "stream" in message.command:
                    return await message.reply_text(_["str_1"])
                buttons = botplaylist_markup(_)
                return await message.reply_photo(
                    photo=PLAYLIST_IMG_URL,
                    caption=_["play_18"],
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
        if message.command[0][0] == "c":
            chat_id = await get_cmode(message.chat.id)
            if chat_id is None:
                return await message.reply_text(_["setting_7"])
            try:
                chat = await app.get_chat(chat_id)
            except:
                return await message.reply_text(_["cplay_4"])
            channel = chat.title
        else:
            chat_id = message.chat.id
            channel = None
        playmode = await get_playmode(message.chat.id)
        playty = await get_playtype(message.chat.id)
        if playty != "Everyone":
            if message.from_user.id not in SUDOERS:
                admins = adminlist.get(message.chat.id)
                if not admins:
                    return await message.reply_text(_["admin_13"])
                else:
                    if message.from_user.id not in admins:
                        return await message.reply_text(_["play_4"])
        if message.command[0][0] == "v" or message.command[0][0] == "ڤ":
            video = True
        else:
            if "-v" in message.text:
                video = True
            else:
                video = True if message.command[0][1] == "v" else None
        if message.command[0][-1] == "e":
            if not await is_active_chat(chat_id):
                return await message.reply_text(_["play_16"])
            fplay = True
        else:
            fplay = None

        if not await is_active_chat(chat_id):
            chat_id = message.chat.id
    userbot = await get_assistant(message.chat.id)
    userbot_id = userbot.id
    done = await message.reply("**✅┋ تکایە کەمێك چاوەڕێ بکە بانگھێشت دەکرێت . .**")
    await asyncio.sleep(1)
    # Get chat member object
    chat_member = await app.get_chat_member(chat_id, app.id)
    
    # Condition 1: Group username is present, bot is not admin
    if message.chat.username and not chat_member.status == ChatMemberStatus.ADMINISTRATOR:
        try:
            await userbot.join_chat(message.chat.username)
            await done.edit_text("**✅┋ بە سەرکەوتوویی یاریدەدەری بۆت جۆینی کرد**")
        except Exception as e:
            await done.edit_text("**🧑🏻‍💻┋ پێویستە ئەدمین بم و ڕۆڵم هەبێت بۆ لادانی باندی یاریدەدەرەکەم**")
            

    # Condition 2: Group username is present, bot is admin, and Userbot is not banned
    if message.chat.username and chat_member.status == ChatMemberStatus.ADMINISTRATOR:
        try:
            await userbot.join_chat(message.chat.username)
            await done.edit_text("**✅┋ بە سەرکەوتوویی یاریدەدەری بۆت جۆینی کرد**")
        except Exception as e:
            await done.edit_text(str(e))

    
    
    # Condition 3: Group username is not present/group is private, bot is admin and Userbot is banned
    if message.chat.username and chat_member.status == ChatMemberStatus.ADMINISTRATOR:
        userbot_member = await app.get_chat_member(chat_id, userbot.id)
        if userbot_member.status in [ChatMemberStatus.BANNED, ChatMemberStatus.RESTRICTED]:
            try:
                await app.unban_chat_member(chat_id, userbot.id)
                await done.edit_text("**✅┋ باندی یاریدەدەر لادەدرێت . .**")
                await userbot.join_chat(message.chat.username)
                await done.edit_text("**👾┋ ئەکاونتی یاریدەدەر باندکراوە، بەڵام ئێستا باندی لادەدەم، دواتر جۆینی گرووپ دەکات ✅**")
            except Exception as e:
                await done.edit_text("**❌┋ شکستی هێنا لە جۆین کردن، تکایە ڕۆڵی باند و بانگھێشت کردنم پێبدە تاوەکو بتوانم ڕاستەوخۆ زیادی بکەمە گرووپ دووبارە بنووسە : /userbotjoin **")
        return
    
    # Condition 4: Group username is not present/group is private, bot is not admin
    if not message.chat.username and not chat_member.status == ChatMemberStatus.ADMINISTRATOR:
        await done.edit_text("**🧑🏻‍💻┋ پێویستە ئەدمین بم بۆ بانگھێشت کردنی یاریدەدەرەکەم**")
        


    # Condition 5: Group username is not present/group is private, bot is admin
    if not message.chat.username and chat_member.status == ChatMemberStatus.ADMINISTRATOR:
        try:
            try:
                userbot_member = await app.get_chat_member(chat_id, userbot.id)
                if userbot_member.status not in [ChatMemberStatus.BANNED, ChatMemberStatus.RESTRICTED]:
                    await done.edit_text("**✅┋ ئەکاونتی یاریدەدەر پێشتر جۆینی کردووە و لە گرووپە**")
                    return
            except Exception as e:
                await done.edit_text("**✅┋ تکایە کەمێك چاوەڕێ بکە بانگھێشت دەکرێت . .**")
                await done.edit_text("**✅┋ تکایە کەمێك چاوەڕێ بکە بانگھێشت دەکرێت . .**")
                invite_link = await app.create_chat_invite_link(chat_id, expire_date=None)
                await asyncio.sleep(2)
                await userbot.join_chat(invite_link.invite_link)
                await done.edit_text("**✅┋ بە سەرکەوتوویی یاریدەدەری بۆت جۆینی کرد**")
        except Exception as e:
            await done.edit_text(f"**💀┋ من یاریدەدەرەکەم دۆزیەوە و وە جۆینی گرووپی نەکردووە بەڵام من ڕۆڵی بانگھێشت کردنی خەڵکیم نییە بۆیە دەبێت ڕۆڵی بانگھێشت کردنم پێبدەیت دواتر دووبارە بنووسیت : /userbotjoin \n\n➥ ئایدی » @{userbot.username} **")

    
    
    # Condition 6: Group username is not present/group is private, bot is admin and Userbot is banned
    if not message.chat.username and chat_member.status == ChatMemberStatus.ADMINISTRATOR:
        userbot_member = await app.get_chat_member(chat_id, userbot.id)
        if userbot_member.status in [ChatMemberStatus.BANNED, ChatMemberStatus.RESTRICTED]:
            try:
                await app.unban_chat_member(chat_id, userbot.id)
                await done.edit_text("**✅┋ ئەکاونتی یاریدەدەر باندی لادرا\nدووبارە بنووسە : /userbotjoin**")
                invite_link = await app.create_chat_invite_link(chat_id, expire_date=None)
                await asyncio.sleep(2)
                await userbot.join_chat(invite_link.invite_link)
                await done.edit_text("**👾┋ ئەکاونتی یاریدەدەر باندکراوە، بەڵام ئێستا باندی لادەدەم، دواتر جۆینی گرووپ دەکات ✅**")
            except Exception as e:
                await done.edit_text(f"**✅┋ من یاریدەدەرەکەم دۆزیەوە و وە باندکراوە لە گرووپ\nبەڵام من ڕۆڵی لادانی باندم نییە\n بۆیە دەبێت ڕۆڵی باند کردنم پێبدەیت\nدواتر دووبارە بنووسیت : /userbotjoin \n\n➥ ئایدی » @{userbot.username} **")
                   
                pass

        return await command(
            client,
            message,
            _,
            chat_id,
            video,
            channel,
            playmode,
            url,
            fplay,
        )

    return wrapper
