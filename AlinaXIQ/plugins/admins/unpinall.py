from pyrogram import filters, enums
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ChatPermissions
)
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    UserAdminInvalid,
    BadRequest
)

import datetime
from AlinaXIQ import app





@app.on_callback_query(filters.regex(r"^unpin"))
async def unpin_callbacc(client, CallbackQuery):
    user_id = CallbackQuery.from_user.id
    name = CallbackQuery.from_user.first_name
    chat_id = CallbackQuery.message.chat.id
    member = await app.get_chat_member(chat_id, user_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_pin_messages:
            pass
        else:
            await CallbackQuery.answer("**ليس من حقك يا عزيزي 🖤•**", show_alert=True)
            return
    else:
        await CallbackQuery.answer("**ليس من حقك يا عزيزي 🖤•**", show_alert=True)
        return
    
    msg_id = CallbackQuery.data.split("=")[1]
    try:
        msg_id = int(msg_id)
    except:
        if msg_id == "yes":
            await client.unpin_all_chat_messages(chat_id)
            textt = "**لقد قمت بحذف جميع الرسائل المعلقة والمثبتة 🖤•**"
        else:
            textt = "**حسنًا، أنا لا أعلق كل الرسائل، ولا أعلقها 🖤•**"

        await CallbackQuery.message.edit_caption(
            textt,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="حذف الدردشة", callback_data="close")]
                ]
            )
        )
        return
        
    await client.unpin_chat_message(chat_id, msg_id)
    await CallbackQuery.message.edit_caption(
        "unpinned!!", 
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="حذف الدردشة", callback_data="close")]
            ]
        )
    )


@app.on_message(filters.command(["unpinall"]))
async def unpin_command_handler(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_pin_messages:
            pass
        else:
            msg_text = "**ليس لك دور في إزالة دبابيس الرسائل 🖤•**"
            return await message.reply_text(msg_text)
    else:
        msg_text = "**ليس لك دور في إزالة دبابيس الرسائل 🖤•**"
        return await message.reply_text(msg_text)
    
    await message.reply_text(
        "**هل أنت متأكد؟ هل تريد إزالة جميع الرسائل المعلقة؟🖤•**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [
                    InlineKeyboardButton(text="نعم", callback_data="unpinall=yes"),
                ],
                [
                    InlineKeyboardButton(text="لا", callback_data="unpinall=no")
                ]
            ]
        )
    )
