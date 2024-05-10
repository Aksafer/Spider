import asyncio
import random
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from AlinaXIQ import app
from strings.filters import command
from config import OWNER_ID
from pyrogram.enums import ParseMode, ChatMemberStatus




iddof = []
@app.on_message(command(['نصيحه']))
def call_random_member(client:Client, message:Message):
    chat_id = message.chat.id
    members = [
        member for member in client.get_chat_members(chat_id)
        if not member.user.is_bot
    ]
    if chat_id in iddof:
        return
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
         f"**-ئهذه لك ♥•\n│ ل {random_member_mention}\عليك أن تحاول ثلاث مرات قبل أن تخيب 🖤•**",
         f"**-هذه لك ♥•\n│ ل {random_member_mention}\nامنح كل يوم فرصة ليكون أفضل يوم في حياتك 🖤•**",
         f"**-هذه لك ♥•\n│ ل {random_member_mention}\nالحكمة تعرف متى تتجاهل الناس 🖤•**",
         f"**-هذه لك ♥•\n│ ل {random_member_mention}\nالهدوء مفتاح القفل القوي 🖤•**",
         f"**-هذه لك ♥•\n│ ل {random_member_mention}\nأنت مسؤول عما تشعر به، لكنك لست مسؤولاً عما يفعله الآخرون.**",
         f"**-هذه لك ♥•\n│ ل {random_member_mention}\nإذا لم تعيش بالطريقة التي تريدها، عليك أن تتغير 🖤•**",
         f"**-هذه لك ♥•\n│ ل {random_member_mention}\nالفائزون لا يخبرون سر تدريباتهم فهم يسيرون نحو الأهداف الكبيرة 🖤•**",
         f"**-هذه لك ♥•\n│ ل {random_member_mention}\nلا يوجد شيء أفضل في الحياة من الحب والسعادة 🖤•**",
         f"**-هذه لك ♥•\n│ ل {random_member_mention}\nعندما تتغير الرياح يجب أن نعدل اتجاه البحر بدلاً من إيقاف الرحلة.**",
         f"**-هذه لك ♥•\n│ ل {random_member_mention}\nالحياة كالموجة، عليك فقط أن تجد توازنك حتى لا تغرق.**",
         f"**-هذه لك ♥•\n│ ل {random_member_mention}\nالشجرة التي تنحني في الريح هي الشجرة التي تنكسر في العاصفة 🖤•**",
         f"**-هذه لك ♥•\n│ ل {random_member_mention}\n أمنيتي أن تكون هناك زاوية خطيرة لا يمكن لشيء أن ينمو بدون مقاومة 🖤•**",
         f"**-هذه لك ♥•\n│ ل {random_member_mention}\nلا يمكنك أن تنسى الظلام عليك أن تصنع شمعة 🖤•**",
         f"**-هذه لك ♥•\n│ ل {random_member_mention}\nللمسافة طعم يأتي من الألم للشخص الذي لم يخسر في الحب 🖤•**",
         f"**-هذه لك ♥•\n│ ل {random_member_mention}\nالأشياء لا يحددها الموقف بل ردود الأفعال على الموقف 🖤•**",
         f"**-هذه لك ♥•\n│ ل {random_member_mention}\nاختر في النهاية طريقاً لم يكن في مصلحتك واترك طريقاً آخر لم يتم العثور عليه.**",
         f"**-هذه لك ♥•\n│ ل {random_member_mention}\nلم يكن لديك شيء جيد لتقوله، لذا اصمت 🖤•**"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id= message.id)
@app.on_message(command(['نداء','ن']))
def call_random_member(client:Client, message:Message):
    chat_id = message.chat.id
    members = [
        member for member in client.get_chat_members(chat_id)
        if not member.user.is_bot
    ]
    if chat_id in iddof:
         return
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
        f"**أنت أجمل منا{random_member_mention}🌚🖤•**",
        f"**جمالك لا يوصف بأي حال من الأحوال لا يمكن القيام بذلك{random_member_mention}⚡♥•**",
        f"**الحب في قلبه هەموواندا{random_member_mention}🍭💞•**",
        f"**تقول يا عزيزي هياا بطخم{random_member_mention}😂♥•**",
        f"**المدينة بجمالكۆ لقد تفاجأ{random_member_mention}🙊🥰•**",
        f"**اجلس وكن غبيا{random_member_mention}😂🤭•**",
        f"**أنت تقول فيلي{random_member_mention}😔😂•**",
         f"**عفوًا، هذا ما يفعلونه{random_member_mention}💘•**",
         f"**تناول بعض الكلامزي فليكن ثقيلاً بیت{random_member_mention}🥰😂😂•**",
         f"**أنت قبيح جداً {random_member_mention}😂😳•**"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id= message.id)
