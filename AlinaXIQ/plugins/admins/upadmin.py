from pyrogram import Client, filters, types, enums
from pyrogram.types import ChatMemberUpdated
from AlinaXIQ import app
import asyncio
import json




ON_TYPES = {True: "✅", False: "❌"}
Temp = {}
ChatPrivileges_Types = {
    'edit_info': False,
    'delete_message': False,
    'restrict_members': False,
    'invite_users': False,
    'pin_message': False,
    'Manage_video': False,
    'promote_members': False, }



# Pyrogrma Filters Create .
def is_admin():
    async def func(_, app, message):
        user_id = message.from_user.id
        try:
            chat_id = message.chat.id
        except AttributeError as e:
            chat_id = message.message.chat.id
        Res = await app.get_chat_member(chat_id, user_id)
        return Res.status == enums.ChatMemberStatus.OWNER or Res.status == enums.ChatMemberStatus.ADMINISTRATOR or message.from_user.id != "6816180621"

    return filters.create(func)


def is_onCall(data):
    async def func(flt, _, query):
        return query.data.split('|')[0] == flt.data

    return filters.create(func, data=data)


# Keyboard UP Admin
def keyboard(user_id: int):
    return types.InlineKeyboardMarkup([
        [
            types.InlineKeyboardButton(ON_TYPES[False if False in Temp[user_id].values() else True],
                                       f"up_all_prom|" + json.dumps({'user_id': user_id})),
            types.InlineKeyboardButton('جميع الصلاحيات', 'None')
        ], [
            types.InlineKeyboardButton(ON_TYPES[Temp[user_id]['edit_info']],
                                       f"up_prom|" + json.dumps({'user_id': user_id, 'promote': 'edit_info'})),
            types.InlineKeyboardButton('تغير معلومات الجروب', 'None')
        ], [
            types.InlineKeyboardButton(ON_TYPES[Temp[user_id]['delete_message']],
                                       f"up_prom|" + json.dumps({'user_id': user_id, 'promote': 'delete_message'})),
            types.InlineKeyboardButton('حذف الرسائل', 'None')
        ], [
            types.InlineKeyboardButton(ON_TYPES[Temp[user_id]['restrict_members']],
                                       f"up_prom|" + json.dumps({'user_id': user_id, 'promote': 'restrict_members'})),
            types.InlineKeyboardButton('حظر المستخدمين', 'None'),
        ], [
            types.InlineKeyboardButton(ON_TYPES[Temp[user_id]['pin_message']],
                                       f"up_prom|" + json.dumps({'user_id': user_id, 'promote': 'pin_message'})),
            types.InlineKeyboardButton('دعوه المستخدمين', 'None')
        ], [
            types.InlineKeyboardButton(ON_TYPES[Temp[user_id]['Manage_video']],
                                       f"up_prom|" + json.dumps({'user_id': user_id, 'promote': 'Manage_video'})),
            types.InlineKeyboardButton('اداره البث المباشر', 'None')
        ], [
            types.InlineKeyboardButton(ON_TYPES[Temp[user_id]['promote_members']],
                                       f"up_prom|" + json.dumps({'user_id': user_id, 'promote': 'promote_members'})),
            types.InlineKeyboardButton('رفع مشرفين', 'None')
        ], [
            types.InlineKeyboardButton('اضغط للرفع الي مشرف', f"save|" + json.dumps({'user_id': user_id}))
        ], [
            types.InlineKeyboardButton(text='اغلاق', callback_data="close"),
        ], ])





# /up_admin WIth Group .
@app.on_message(filters.regex('^/admin$') & filters.group & filters.reply & is_admin())
async def ON_RPLY(app: Client, Message: types.Message):
    chat_id, message_id, user_id = Message.chat.id, Message.id, Message.from_user.id
    member_up_id = Message.reply_to_message.from_user.id
    Stateus = await app.get_chat_member(chat_id, member_up_id)
    Temp.update({member_up_id: ChatPrivileges_Types})
    await app.send_message(chat_id, text='قم بتعيين أدوار إدارية جديدة ثم قم بتعيينه كمشرف•',
                           reply_markup=keyboard(member_up_id))


@app.on_callback_query(is_onCall('up_prom') & is_admin())
async def Call_Up(app: Client, query: types.CallbackQuery):
    ONE = {True: False, False: True}
    JSobj = json.loads(query.data.split('|')[1])
    Temp[JSobj['user_id']][JSobj['promote']] = ONE[Temp[JSobj['user_id']][JSobj['promote']]]
    await app.edit_message_text(text='قم بتعيين أدوار إدارية جديدة ثم قم بتعيينه كمشرف•',
                                reply_markup=keyboard(JSobj['user_id']), chat_id=query.message.chat.id,
                                message_id=query.message.id)


@app.on_callback_query(is_onCall('up_all_prom') & is_admin())
async def Call_Up(app: Client, query: types.CallbackQuery):
    JSobj = json.loads(query.data.split('|')[1])
    for P in Temp[JSobj['user_id']]:
        Temp[JSobj['user_id']][P] = True
    await app.edit_message_text(text='قم بتعيين أدوار إدارية جديدة ثم قم بتعيينه كمشرف•',
                                reply_markup=keyboard(JSobj['user_id']), chat_id=query.message.chat.id,
                                message_id=query.message.id)


@app.on_callback_query(is_onCall('save'))
async def Call_Up(app: Client, query: types.CallbackQuery):
    JSobj = json.loads(query.data.split('|')[1])
    chat_id = query.message.chat.id
    try:
        await app.promote_chat_member(chat_id, JSobj['user_id']
                                      , types.ChatPrivileges(
                can_change_info=Temp[JSobj['user_id']]['edit_info'],
                can_delete_messages=Temp[JSobj['user_id']]['delete_message'],
                can_restrict_members=Temp[JSobj['user_id']]['restrict_members'],
                can_invite_users=Temp[JSobj['user_id']]['invite_users'],
                can_pin_messages=Temp[JSobj['user_id']]['pin_message'],
                can_manage_video_chats=Temp[JSobj['user_id']]['Manage_video'],
                can_promote_members=Temp[JSobj['user_id']]['promote_members']
            ))
        await app.edit_message_text(text='✧¦ تم إنشاء المشرف بنجاح•', chat_id=query.message.chat.id,
                                    message_id=query.message.id)
    except ChatAdminRequired as Err:
        await app.edit_message_text(text='✧¦ يجب أن تكون مشرفا في هاذه المجموعه',
                                    chat_id=query.message.chat.id, message_id=query.message.id)
    await asyncio.sleep(60)
    await app.delete_messages(query.message.chat.id, query.message.id)
