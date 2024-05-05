import asyncio
from typing import Optional
from random import randint
from pyrogram.types import Message, ChatPrivileges
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from AlinaXIQ.utils.database import *
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant, ChatAdminRequired
from AlinaXIQ import app , Userbot
from AlinaXIQ.utils.alina_ban import admin_filter

async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    assistant = await get_assistant(message.chat.id)
    chat_peer = await assistant.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await assistant.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await assistant.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await app.send_message(f"**لم يتم إجراء أي مكالمات إلى المجموعة** {err_msg}")
    return False

@app.on_message(command(["/open", "افتح كول", "فتح كول"]) & admin_filter & ~filters.private)
async def start_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    assistant = await get_assistant(chat_id)
    ass = await assistant.get_me()
    assid = ass.id
    if assistant is None:
        await app.send_message(chat_id, "خطأ في المساعدة")
        return
    msg = await app.send_message(chat_id, "•⎆┊**أخبرني مرة أخرى...♥**")
    try:
        peer = await assistant.resolve_peer(chat_id)
        await assistant.invoke(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=assistant.rnd_id() // 9000000000,
            )
        )
        await msg.edit_text("•⎆┊**تم فتح الكول بنجاح♥⚡️•**")
    except ChatAdminRequired:
      try:    
        await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                can_manage_chat=False,
                can_delete_messages=False,
                can_manage_video_chats=True,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False,
            ),
        )
        peer = await assistant.resolve_peer(chat_id)
        await assistant.invoke(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=assistant.rnd_id() // 9000000000,
            )
        )
        await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            ),
        )                              
        await msg.edit_text("•⎆┊**تم فتح الكول بنجاح♥⚡️•**")
      except:
         await msg.edit_text("•⎆┊**ضع البوت يلعب دور إضافة مسؤول والتحكم في المكالمه أو السماح للمساعد بالمحاولة🕷•**")
        
@app.on_message(command(["/close", "اقفل كول", "قفل كول"]) & admin_filter & ~filters.private)
async def stop_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    assistant = await get_assistant(chat_id)
    ass = await assistant.get_me()
    assid = ass.id
    if assistant is None:
        await app.send_message(chat_id, "خطأ في المساعدة")
        return
    msg = await app.send_message(chat_id, "•⎆┊**الهاتف مغلق .. ♥ .**")
    try:
        if not (
           group_call := (
               await get_group_call(assistant, m, err_msg="⎆┊**انتهى التلي جروب ♥•**")
           )
        ):  
           return
        await assistant.invoke(DiscardGroupCall(call=group_call))
        await msg.edit_text("•⎆┊**تم قفل الكول بنجاح♥⚡️•**")
    except Exception as e:
      if "GROUPCALL_FORBIDDEN" in str(e):
       try:    
         await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
                can_manage_chat=False,
                can_delete_messages=False,
                can_manage_video_chats=True,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False,
             ),
         )
         if not (
           group_call := (
               await get_group_call(assistant, m, err_msg="•⎆┊**انتهى التلي جروب ♥•**")
           )
         ):  
           return
         await assistant.invoke(DiscardGroupCall(call=group_call))
         await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            ),
         )                              
         await msg.edit_text("•⎆┊**تم قفل الكول بنجاح♥⚡️•**")
       except:
         await msg.edit_text("•⎆┊**ضع البوت يلعب دور إضافة مسؤول والتحكم في المكالمه أو السماح للمساعد بالمحاولة🕷•**")
    
