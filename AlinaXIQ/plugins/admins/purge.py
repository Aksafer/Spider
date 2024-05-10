from asyncio import sleep
from pyrogram import filters
from pyrogram.enums import ChatType
from AlinaXIQ.misc import SUDOERS
from pyrogram.errors import MessageDeleteForbidden, RPCError
from pyrogram.types import Message
from AlinaXIQ.utils.alina_ban import admin_filter
from AlinaXIQ import app


@app.on_message(filters.command("purge") & admin_filter)
async def purge(app: app, msg: Message):
    
    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="**لا أستطيع حذف الرسائل في مجموعة أساسية أنشئ مجموعة عامة🖤•**")
        return

    if msg.reply_to_message:
        message_ids = list(range(msg.reply_to_message.id, msg.id))

        def divide_chunks(l: list, n: int = 100):
            for i in range(0, len(l), n):
                yield l[i : i + n]

        
        m_list = list(divide_chunks(message_ids))

        try:
            for plist in m_list:
                await app.delete_messages(chat_id=msg.chat.id, message_ids=plist, revoke=True)
                
            await msg.delete()
        except MessageDeleteForbidden:
            await msg.reply_text(text="**لا أستطيع حذف جميع الرسائل، قد تكون قديمة أو قد لا أملك الحق أو الدور في حذفها أو قد لا تكون مجموعة عامة 🖤•**")
            return
            
        except RPCError as ef:
            await msg.reply_text(text=f"**هناك بعض الأخطاء، الإبلاغ عنها باستخدامه** `/bug`<b>خطأ:</b> <code>{ef}</code>")
        count_del_msg = len(message_ids)
        sumit = await msg.reply_text(text=f"**تم حذفه <i>{count_del_msg}</i> خطاب**")
        await sleep(3)
        await sumit.delete()
        return
    await msg.reply_text("**قم بالرد على الرسالة لبدء التعبئة**")
    return





@app.on_message(filters.command("spurge") & admin_filter)
async def spurge(app: app, msg: Message):

    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="**لا أستطيع حذف الرسائل في مجموعة أساسية أنشئ مجموعة عامة🖤•**")
        return

    if msg.reply_to_message:
        message_ids = list(range(msg.reply_to_message.id, msg.id))

        def divide_chunks(l: list, n: int = 100):
            for i in range(0, len(l), n):
                yield l[i : i + n]

        m_list = list(divide_chunks(message_ids))

        try:
            for plist in m_list:
                await app.delete_messages(chat_id=msg.chat.id, message_ids=plist, revoke=True)
            await msg.delete()
        except MessageDeleteForbidden:
            await msg.reply_text(text="**لا أستطيع حذف جميع الرسائل، قد تكون قديمة أو قد لا أملك الحق أو الدور في حذفها أو قد لا تكون مجموعة عامة 🖤•**")
            return
            
        except RPCError as ef:
            await msg.reply_text(text=f"**هناك بعض الأخطاء، الإبلاغ عنها باستخدامه** `/bug`<b>خطأ:</b> <code>{ef}</code>")           
            return        
    await msg.reply_text("**قم بالرد على الرسالة لبدء التعبئة**")
    return


@app.on_message(filters.command("del") & admin_filter)
async def del_msg(app: app, msg: Message):
    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="**لا أستطيع حذف الرسائل في مجموعة أساسية أنشئ مجموعة عامة🖤•*")
        return        
    if msg.reply_to_message:
        await msg.delete()
        await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.reply_to_message.id)
    else:
        await msg.reply_text(text="**ماذا تريد أن تحذف 🖤؟**")
        return
