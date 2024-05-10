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
from AlinaXIQ.misc import SUDOERS
import datetime
from AlinaXIQ import app




def mention(user, name, mention=True):
    if mention == True:
        link = f"[{name}](tg://openmessage?user_id={user})"
    else:
        link = f"[{name}](https://t.me/{user})"
    return link



async def get_userid_from_username(username):
    try:
        user = await app.get_users(username)
    except:
        return None
    
    user_obj = [user.id, user.first_name]
    return user_obj


async def ban_user(user_id, first_name, admin_id, admin_name, chat_id, reason, time=None):
    try:
        await app.ban_chat_member(chat_id, user_id)
    except ChatAdminRequired:
        msg_text = "ليس لدي جميع الصلاحيات، الكافيه لحظرو •"
        return msg_text, False
    except UserAdminInvalid:
        msg_text = "لا يمكنني طرد المشرف من الجروب"
        return msg_text, False
    except Exception as e:
        if user_id in SUDOERS:
            msg_text = "لا أستطيع طرد المطور"
            return msg_text, False
        
        msg_text = f"لا يمكنني ان اطرد نفسي"
        return msg_text, False

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)

    msg_text += f"تمت إزالته: {user_mention}\nبواسطة: {admin_mention}**"
    
    if reason:
        msg_text += f"سبب: `{reason}`\n**"
    if time:
        msg_text += f"وقت: `{time}`\n**"

    return msg_text, True


async def unban_user(user_id, first_name, admin_id, admin_name, chat_id):
    try:
        await app.unban_chat_member(chat_id, user_id)
    except ChatAdminRequired:
        msg_text = "ليس لدي الصلاحيات الكافيه لفعل ذالك"
        return msg_text
    except Exception as e:
        msg_text = f"لا يمكنني ان اطرد نفسي"
        return msg_text

    user_mention = mention(user_id, first_name)
    admin_mention = mention(admin_id, admin_name)
    
    msg_text = f"تمت ازالته: {user_mention}\nبواسطة: {admin_mention}**"
    return msg_text


    


@app.on_message(filters.command(["حظر","طرد"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def ban_command_handler(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_restrict_members:
            pass
        else:
            msg_text = "ليس لديك الصلاحيات لطرد أو حظر شخص ما•"
            return await message.reply_text(msg_text)
    else:
        msg_text = "ليس لديك الصلاحيات لطرد أو حظر شخص ما•"
        return await message.reply_text(msg_text)

    # Extract the user ID from the command or reply
    if len(message.command) > 1:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            first_name = message.reply_to_message.from_user.first_name
            reason = message.text.split(None, 1)[1]
        else:
            try:
                user_id = int(message.command[1])
                first_name = "User"
            except:
                user_obj = await get_userid_from_username(message.command[1])
                if user_obj == None:
                    return await message.reply_text("لا أستطيع العثور على المستخدم")
                user_id = user_obj[0]
                first_name = user_obj[1]

            try:
                reason = message.text.partition(message.command[1])[2]
            except:
                reason = None

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        reason = None
    else:
        await message.reply_text("الرجاء إدخال اسم المستخدم الخاص بالمستخدم مع الأمر أو الرد على رسالة ذلك المستخدم•")
        return
        
    msg_text, result = await ban_user(user_id, first_name, admin_id, admin_name, chat_id, reason)
    if result == True:
        await message.reply_text(msg_text)
    if result == False:
        await message.reply_text(msg_text)



@app.on_message(filters.command(["حظر","باند"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def unban_command_handler(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_restrict_members:
            pass
        else:
            msg_text = "ليس لديك الصلاحيات لطرد أو حظر شخص ما•"
            return await message.reply_text(msg_text)
    else:
        msg_text = "ليس لديك الصلاحيات لطرد أو حظر شخص ما•"
        return await message.reply_text(msg_text)

    # Extract the user ID from the command or reply
    if len(message.command) > 1:
        try:
            user_id = int(message.command[1])
            first_name = "User"
        except:
            user_obj = await get_userid_from_username(message.command[1])
            if user_obj == None:
                    return await message.reply_text("لا أستطيع العثور على الشخص•")
            user_id = user_obj[0]
            first_name = user_obj[1]

    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
    else:
        await message.reply_text("الرجاء إدخال اسم المستخدم الخاص بالمستخدم مع الأمر أو الرد على رسالة ذلك المستخدم•")
        return
        
    msg_text = await unban_user(user_id, first_name, admin_id, admin_name, chat_id)
    await message.reply_text(msg_text)



@app.on_message(filters.command(["tmute"]))
async def tmute_command_handler(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_restrict_members:
            pass
        else:
            msg_text = "You dont have permission to mute someone"
            return await message.reply_text(msg_text)
    else:
        msg_text = "You dont have permission to mute someone"
        return await message.reply_text(msg_text)

    # Extract the user ID from the command or reply
    if len(message.command) > 1:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            first_name = message.reply_to_message.from_user.first_name
            time = message.text.split(None, 1)[1]

            try:
                time_amount = time.split(time[-1])[0]
                time_amount = int(time_amount)
            except:
                return await message.reply_text("wrong format!!\nFormat: `/tmute 2m`")

            if time[-1] == "m":
                mute_duration = datetime.timedelta(minutes=time_amount)
            elif time[-1] == "h":
                mute_duration = datetime.timedelta(hours=time_amount)
            elif time[-1] == "d":
                mute_duration = datetime.timedelta(days=time_amount)
            else:
                return await message.reply_text("wrong format!!\nFormat:\nm: Minutes\nh: Hours\nd: Days")
        else:
            try:
                user_id = int(message.command[1])
                first_name = "User"
            except:
                user_obj = await get_userid_from_username(message.command[1])
                if user_obj == None:
                    return await message.reply_text("I can't find that user")
                user_id = user_obj[0]
                first_name = user_obj[1]

            try:
                time = message.text.partition(message.command[1])[2]
                try:
                    time_amount = time.split(time[-1])[0]
                    time_amount = int(time_amount)
                except:
                    return await message.reply_text("wrong format!!\nFormat: `/tmute 2m`")

                if time[-1] == "m":
                    mute_duration = datetime.timedelta(minutes=time_amount)
                elif time[-1] == "h":
                    mute_duration = datetime.timedelta(hours=time_amount)
                elif time[-1] == "d":
                    mute_duration = datetime.timedelta(days=time_amount)
                else:
                    return await message.reply_text("wrong format!!\nFormat:\nm: Minutes\nh: Hours\nd: Days")
            except:
                return await message.reply_text("Please specify a valid user or reply to that user's message\nFormat: `/tmute @user 2m`")

    else:
        await message.reply_text("Please specify a valid user or reply to that user's message\nFormat: /tmute <username> <time>")
        return
    
    msg_text, result = await mute_user(user_id, first_name, admin_id, admin_name, chat_id, reason=None, time=mute_duration)
    if result == True:
        await message.reply_text(msg_text)
    if result == False:
        await message.reply_text(msg_text)
