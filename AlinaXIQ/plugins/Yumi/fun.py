import asyncio
import random
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from AlinaXIQ import app
from strings.filters import command
from config import OWNER_ID
from pyrogram.enums import ParseMode, ChatMemberStatus




iddof = []
@app.on_message(command(['خطاب']))
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
         f"**-هذا لك ♥•\n│ بالنسبة إلى {random_member_mention}\nعليك المحاولة ثلاث مرات قبل أن تصاب بخيبة الأمل🖤•**"،
         f"**-هذا لك ♥•\n│ {random_member_mention}\nامنح كل يوم فرصة ليكون أفضل يوم في حياتك🖤•**"،
         f"**-هذه لك ♥•\n│ لـ {random_member_mention}\nالحكمة تعرف متى تتجاهل الأشخاص🖤•**"،
         f"**-هذه لك ♥•\n│ {random_member_mention}\nالهدوء مفتاح القفل القوي🖤•**"،
         f"**-هذا لك ♥•\n│ لـ {random_member_mention}\nأنت مسؤول عما تشعر به، لكنك لست مسؤولاً عما يفعله الآخرون🖤•**"،
         f"**-هذا لك ♥•\n│ من أجل {random_member_mention}\nإذا كنت لا تعيش بالطريقة التي تريدها، عليك تغييرها🖤•**"،
         f"**-هذا من أجلك♥•\n│ لـ {random_member_mention}\nالفائزون لا يخبرون سر تدريبهم إنهم يتجهون نحو الأهداف الكبيرة🖤•**"،
         f"**-هذه لك ♥•\n│ لـ {random_member_mention}\nلا يوجد شيء أفضل في الحياة من الحب والسعادة🖤•**"،
         f"**-هذا لك ♥•\n│ لـ {random_member_mention}\nعندما تتغير الرياح علينا تعديل اتجاه البحر بدلاً من إيقاف الرحلة🖤•**"،
         f"**-هذا من أجلك♥•\n│ لـ {random_member_mention}\nالحياة مثل الموجة، عليك فقط أن تجد توازنك حتى لا تغرق🖤•**"،
         f"**-هذه لك ♥•\n│ لـ {random_member_mention}\nالشجرة التي تنحني في الريح هي الشجرة التي تنكسر في العاصفة🖤•**"،
         f"**-هذا البيان لك♥•\n│ لـ {random_member_mention}\n أمنيتي أن تكون هناك زاوية خطيرة لا شيء يمكن أن ينمو بدون مقاومة🖤•**"،
         f"**-هذا لك ♥•\n│ من أجل {random_member_mention}\nلا يمكنك نسيان الظلام عليك أن تصنع شمعة🖤•**"،
         f"**-هذا لك ♥•\n│ لـ {random_member_mention}\nللمسافة طعم يأتي من الألم للشخص الذي لم يضيع في الحب🖤•**"،
         f"**-هذا لك ♥•\n│ لـ {random_member_mention}\nالأشياء لا تُحدد بالمرور بموقف ما بل بالإجابة على ذلك الموقف🖤•**"،
         f"**-هذا البيان لك♥•\n│ {random_member_mention}\nلاختيارك، في النهاية، طريقاً لم يكن في مصلحتك اترك طريقاً آخر لم يتم العثور عليه🖤•**"،
         f"**-هذه لك ♥•\n│ من أجل {random_member_mention}\nلم يكن لديك أي شيء جيد لتقوله، لذا اصمت🖤•**"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id= message.id)
@app.on_message(command(['وصف','و']))
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
        f"**أنت أجمل منا{random_member_mention}🌚🖤•**"،
        f"**جمالك لا يمكن وصفه بأي شكل من الأشكال{random_member_mention}⚡♥•**"،
        f"**الحب في قلب الجميع{random_member_mention}🍭💞•**"،
        f"**عزيزتي، تعالي وكليني{random_member_mention}😂♥•**"،
        f"**المدينة انذهلت بجمالك{random_member_mention}🙊🥰•**"،
        f"**ذكر_العضو_العشوائي}😂🤭•**"،
        f"**إنه مثل الفيل{random_ member_mention} 😢😂•**"،
         f"**أف هذا ما {random_member_mention}💘•**"،
         f"**تناول بعض الكلمات لتكون ثقيلة{random_member_mention}🥰😂😂•**"،
         f"**أنا قبيح جدًا {random_member_mention}😂😳•**"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id= message.id)
