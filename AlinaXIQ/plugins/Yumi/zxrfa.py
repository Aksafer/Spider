
import random
import re
from config import BOT_NAME 
from strings.filters import command
from pyrogram import Client
from pyrogram.types import Message
from AlinaXIQ import app

@app.on_message(command("ز"))
async def zahrafa(c: Client, m: Message):
    text_list = m.text.split(None, 1)
    if len(text_list) < 2:
        await m.reply_text("**◍ هەڵەیە دووبارە هەوڵبدەوە\n\nبەم شێوازە بینووسە : `ز محمد` √**", reply_to_message_id=m.id)
        return
    text = text_list[1].split(None, 1)[1] if len(text_list[1].split()) > 1 else text_list[1]
    if len(text) > 20:
        await m.reply_text("**◍ ناتوانم زیاتر لە 𝟐𝟎 پیت دروست بکەم، دووبارە هەوڵبدەوە\n√**", reply_to_message_id=m.id)
        return

    # هنا يتم تنفيذ زخرفة النص


    else:
        if re.match("\n", str(m.text)):
            await m.reply_text("**◍ ناتوانم دەقێك بڕازێنمەوە ئەگەر دوو دێڕ بێت\n√**", reply_to_message_id=m.id)
            return
    EmojeS = [
        ' 𓁻',
        ' 𓏴  ',
        ' 𓏶 ',
        ' 𓏡',
        ' 𓏢',
        ' 𓏣',
        ' ☽‘',
        ' 𖠱☂',
        '◑',
        ' ◌“',
        ' ★℡',
        ' ☆'
    ]
    Emoje = [
        ' ♕',
        ' 𖤍',
        '˛𖤓',
        '✾ ☫',
        ' ♫ ',
        ' ❈ ',
        ' ➽',
        ' ✺',
        '  ⚘',
        ' 𖤐',
        ' ❣',
        ' ❿  '
    ]

    zhrf = re.sub('ض', 'ضِٰـِۢ', text)
    zhrf = re.sub('ص', 'صِٰـِۢ', zhrf)
    zhrf = re.sub('ث', 'ثِٰـِۢ', zhrf)
    zhrf = re.sub('ق', 'قِٰـِۢ', zhrf)
    zhrf = re.sub('ف', 'فِٰ͒ـِۢ', zhrf)
    zhrf = re.sub('غ', 'غِٰـِۢ', zhrf)
    zhrf = re.sub('ع', 'عِٰـِۢ', zhrf)
    zhrf = re.sub('خ', 'خِٰ̐ـِۢ', zhrf)
    zhrf = re.sub('ح', 'حِٰـِۢ', zhrf)
    zhrf = re.sub('ج', 'جِٰـِۢ', zhrf)
    zhrf = re.sub('ش', 'شِٰـِۢ', zhrf)
    zhrf = re.sub('س', 'سِٰـِۢ', zhrf)
    zhrf = re.sub('ي', 'يِٰـِۢ', zhrf)
    zhrf = re.sub('ب', 'بِٰـِۢ', zhrf)
    zhrf = re.sub('ل', 'لِٰـِۢ', zhrf)
    zhrf = re.sub('ا', 'آ', zhrf)
    zhrf = re.sub('ت', 'تِٰـِۢ', zhrf)
    zhrf = re.sub('ن', 'نِٰـِۢ', zhrf)
    zhrf = re.sub('م', 'مِٰـِۢ', zhrf)
    zhrf = re.sub('ك', 'ڪِٰـِۢ', zhrf)
    zhrf = re.sub('ط', 'طِٰـِۢ', zhrf)
    zhrf = re.sub('ظ', 'ظِٰـِۢ', zhrf)
    zhrf = re.sub('ء', 'ء', zhrf)
    zhrf = re.sub('ؤ', 'ؤ', zhrf)
    zhrf = re.sub('ر', 'ر', zhrf)
    zhrf = re.sub('ى', 'ى', zhrf)
    zhrf = re.sub('ز', 'ز', zhrf)
    zhrf = re.sub('و', 'ﯛ̲୭', zhrf)
    zhrf = re.sub('ه', 'ۿۿہ', zhrf)
    zhrf = re.sub('a', '𝗮', zhrf)
    zhrf = re.sub('A', '𝗔', zhrf)
    zhrf = re.sub("b", "𝗯", zhrf)
    zhrf = re.sub("B", "𝗕", zhrf)
    zhrf = re.sub("c", "𝗰", zhrf)
    zhrf = re.sub("C", "𝗖", zhrf)
    zhrf = re.sub("d", "𝗱", zhrf)
    zhrf = re.sub("D", "𝗗", zhrf)
    zhrf = re.sub("e", "𝗲", zhrf)
    zhrf = re.sub("E", "𝗘", zhrf)
    zhrf = re.sub("f", "𝗳", zhrf)
    zhrf = re.sub("F", "𝗙", zhrf)
    zhrf = re.sub("g", "𝗴", zhrf)
    zhrf = re.sub("G", "𝗚", zhrf)
    zhrf = re.sub("h", "𝗵", zhrf)
    zhrf = re.sub("H", "𝗛", zhrf)
    zhrf = re.sub("i", "𝗹", zhrf)
    zhrf = re.sub("I", "𝗜", zhrf)
    zhrf = re.sub("j", "𝗝", zhrf)
    zhrf = re.sub("J", "𝗝", zhrf)
    zhrf = re.sub("k", "𝗸", zhrf)
    zhrf = re.sub("K", "𝗞", zhrf)
    zhrf = re.sub("l", "𝗹", zhrf)
    zhrf = re.sub("L", "𝗟", zhrf)
    zhrf = re.sub("m", "𝗺", zhrf)
    zhrf = re.sub("M", "𝗠", zhrf)
    zhrf = re.sub("n", "𝗻", zhrf)
    zhrf = re.sub("N", "𝗡", zhrf)
    zhrf = re.sub("o", "𝗼", zhrf)
    zhrf = re.sub("O", "𝗢", zhrf)
    zhrf = re.sub("p", "𝗽", zhrf)
    zhrf = re.sub("P", "𝗣", zhrf)
    zhrf = re.sub("q", "𝗾", zhrf)
    zhrf = re.sub("Q", "𝗤", zhrf)
    zhrf = re.sub("r", "𝗿", zhrf)
    zhrf = re.sub("R", "𝗥", zhrf)
    zhrf = re.sub("s", "𝘀", zhrf)
    zhrf = re.sub("S", "𝗦", zhrf)
    zhrf = re.sub("t", "𝘁", zhrf)
    zhrf = re.sub("T", "𝗧", zhrf)
    zhrf = re.sub("u", "𝘂", zhrf)
    zhrf = re.sub("U", "𝗨", zhrf)
    zhrf = re.sub("v", "𝘃", zhrf)
    zhrf = re.sub("V", "𝗩", zhrf)
    zhrf = re.sub("w", "𝘄", zhrf)
    zhrf = re.sub("W", "𝗪", zhrf)
    zhrf = re.sub("x", "𝘅", zhrf)
    zhrf = re.sub("X", "𝗫", zhrf)
    zhrf = re.sub("y", "𝘆", zhrf)
    zhrf = re.sub("Y", "𝗬", zhrf)
    zhrf = re.sub("z", "𝘇", zhrf)
    zhrf = re.sub("Z", "𝗭", zhrf)

    zhrf2 = re.sub('ض', 'ضَٰـُـٰٓ', m.text)
    zhrf2 = re.sub('ص', 'صَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ث', 'ثَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ق', 'قَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ف', 'فَٰ͒ـُـٰٓ', zhrf2)
    zhrf2 = re.sub('غ', 'غَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ع', 'عَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('خ', 'خَٰ̐ـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ح', 'حَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ج', 'جَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ش', 'شَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('س', 'سَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ي', 'يَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ب', 'بَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ل', 'لَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ا', 'آ', zhrf2)
    zhrf2 = re.sub('ت', 'تَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ن', 'نَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('م', 'مَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ك', 'ڪَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ط', 'طَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ظ', 'ظَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ء', 'ء', zhrf2)
    zhrf2 = re.sub('ؤ', 'ؤ', zhrf2)
    zhrf2 = re.sub('ر', 'ر', zhrf2)
    zhrf2 = re.sub('ى', 'ى', zhrf2)
    zhrf2 = re.sub('ز', 'ز', zhrf2)
    zhrf2 = re.sub('و', 'ﯛ̲୭', zhrf2)
    zhrf2 = re.sub("ه", "ۿۿہ", zhrf2)
    zhrf2 = re.sub('a', "𝖆", zhrf2)
    zhrf2 = re.sub('A', "𝖆", zhrf2)
    zhrf2 = re.sub("b", "𝖇", zhrf2)
    zhrf2 = re.sub("B", "𝖇", zhrf2)
    zhrf2 = re.sub("c", "𝖈", zhrf2)
    zhrf2 = re.sub("C", "𝖈", zhrf2)
    zhrf2 = re.sub("d", "𝖉", zhrf2)
    zhrf2 = re.sub("D", "𝖉", zhrf2)
    zhrf2 = re.sub("e", "𝖊", zhrf2)
    zhrf2 = re.sub("E", "𝖊", zhrf2)
    zhrf2 = re.sub("f", "𝖋", zhrf2)
    zhrf2 = re.sub("F", "𝖋", zhrf2)
    zhrf2 = re.sub("g", "𝖌", zhrf2)
    zhrf2 = re.sub("G", "𝖌", zhrf2)
    zhrf2 = re.sub("h", "𝖍", zhrf2)
    zhrf2 = re.sub("H", "𝖍", zhrf2)
    zhrf2 = re.sub("i", "𝖎", zhrf2)
    zhrf2 = re.sub("I", "𝖎", zhrf2)
    zhrf2 = re.sub("j", "𝖏", zhrf2)
    zhrf2 = re.sub("J", "𝖏", zhrf2)
    zhrf2 = re.sub("k", "𝖐", zhrf2)
    zhrf2 = re.sub("K", "𝖐", zhrf2)
    zhrf2 = re.sub("l", "𝖑", zhrf2)
    zhrf2 = re.sub("L", "𝖑", zhrf2)
    zhrf2 = re.sub("m", "𝖒", zhrf2)
    zhrf2 = re.sub("M", "𝖒", zhrf2)
    zhrf2 = re.sub("n", "𝖓", zhrf2)
    zhrf2 = re.sub("N", "𝖓", zhrf2)
    zhrf2 = re.sub("o", "𝖔", zhrf2)
    zhrf2 = re.sub("O", "𝖔", zhrf2)
    zhrf2 = re.sub("p", "𝖕", zhrf2)
    zhrf2 = re.sub("P", "𝖕", zhrf2)
    zhrf2 = re.sub("q", "𝖖", zhrf2)
    zhrf2 = re.sub("Q", "𝖖", zhrf2)
    zhrf2 = re.sub("r", "𝖗", zhrf2)
    zhrf2 = re.sub("R", "𝖗", zhrf2)
    zhrf2 = re.sub("s", "𝖘", zhrf2)
    zhrf2 = re.sub("S", "𝖘", zhrf2)
    zhrf2 = re.sub("t", "𝖙", zhrf2)
    zhrf2 = re.sub("T", "𝖙", zhrf2)
    zhrf2 = re.sub("u", "𝖚", zhrf2)
    zhrf2 = re.sub("U", "𝖚", zhrf2)
    zhrf2 = re.sub("v", "𝖛", zhrf2)
    zhrf2 = re.sub("V", "𝖛", zhrf2)
    zhrf2 = re.sub("w", "𝖜", zhrf2)
    zhrf2 = re.sub("W", "𝖜", zhrf2)
    zhrf2 = re.sub("x", "𝖝", zhrf2)
    zhrf2 = re.sub("X", "𝖝", zhrf2)
    zhrf2 = re.sub("y", "𝖞", zhrf2)
    zhrf2 = re.sub("Y", "𝖞", zhrf2)
    zhrf2 = re.sub("z", "𝖟", zhrf2)
    zhrf2 = re.sub("Z", "𝖟", zhrf2)

    zhrf3 = re.sub('ض', 'ض', m.text)
    zhrf3 = re.sub('ص', 'ص', zhrf3)
    zhrf3 = re.sub('ث', 'ثہ', zhrf3)
    zhrf3 = re.sub('ق', 'ق', zhrf3)
    zhrf3 = re.sub('ف', 'فُہ', zhrf3)
    zhrf3 = re.sub('غ', 'غہ', zhrf3)
    zhrf3 = re.sub('ع', 'عہ', zhrf3)
    zhrf3 = re.sub('ه', 'هٰہٰٖ', zhrf3)
    zhrf3 = re.sub('خ', 'خہ', zhrf3)
    zhrf3 = re.sub('ح', 'حہ', zhrf3)
    zhrf3 = re.sub('ج', 'جہ', zhrf3)
    zhrf3 = re.sub('د', 'د', zhrf3)
    zhrf3 = re.sub('ذ', 'ذ', zhrf3)
    zhrf3 = re.sub('ش', 'شہ', zhrf3)
    zhrf3 = re.sub('س', 'سہ', zhrf3)
    zhrf3 = re.sub('ي', 'يہ', zhrf3)
    zhrf3 = re.sub('ب', 'بّ', zhrf3)
    zhrf3 = re.sub('ل', 'لہ', zhrf3)
    zhrf3 = re.sub('ا', 'ا', zhrf3)
    zhrf3 = re.sub('ت', 'تہ', zhrf3)
    zhrf3 = re.sub('ن', 'نٰہٰٖ', zhrf3)
    zhrf3 = re.sub('م', 'مٰہٰٖ', zhrf3)
    zhrf3 = re.sub('ك', 'كُہ', zhrf3)
    zhrf3 = re.sub('ط', 'طہ', zhrf3)
    zhrf3 = re.sub('ئ', 'ئ ْٰ', zhrf3)
    zhrf3 = re.sub('ء', 'ء', zhrf3)
    zhrf3 = re.sub('ؤ', 'ؤ', zhrf3)
    zhrf3 = re.sub('ر', 'رَ', zhrf3)
    zhrf3 = re.sub('لا', 'لہا', zhrf3)
    zhrf3 = re.sub('ى', 'ىْ', zhrf3)
    zhrf3 = re.sub('ة', 'ة', zhrf3)
    zhrf3 = re.sub('و', 'و', zhrf3)
    zhrf3 = re.sub('ز', 'ز', zhrf3)
    zhrf3 = re.sub('ظ', 'ظۗہٰٰ', zhrf3)
    zhrf3 = re.sub('q', '𝐪', zhrf3)
    zhrf3 = re.sub('Q', '𝐪', zhrf3)
    zhrf3 = re.sub('w', '𝐰', zhrf3)
    zhrf3 = re.sub('W', '𝐰', zhrf3)
    zhrf3 = re.sub('e', '𝐞', zhrf3)
    zhrf3 = re.sub('E', '𝐞', zhrf3)
    zhrf3 = re.sub('r', '𝐫', zhrf3)
    zhrf3 = re.sub('R', '𝐫', zhrf3)
    zhrf3 = re.sub('t', '𝐭', zhrf3)
    zhrf3 = re.sub('T', '𝐭', zhrf3)
    zhrf3 = re.sub('y', '𝐲', zhrf3)
    zhrf3 = re.sub('Y', '𝐲', zhrf3)
    zhrf3 = re.sub('u', '𝐮', zhrf3)
    zhrf3 = re.sub('i', '𝐢', zhrf3)
    zhrf3 = re.sub('o', '𝐨', zhrf3)
    zhrf3 = re.sub('p', '𝐩', zhrf3)
    zhrf3 = re.sub('a', '𝐚', zhrf3)
    zhrf3 = re.sub('s', '𝐬', zhrf3)
    zhrf3 = re.sub('d', '𝐝', zhrf3)
    zhrf3 = re.sub('f', '𝐟', zhrf3)
    zhrf3 = re.sub('g', '𝐠', zhrf3)
    zhrf3 = re.sub('h', '𝐡', zhrf3)
    zhrf3 = re.sub('j', '𝐣', zhrf3)
    zhrf3 = re.sub('k', '𝐤', zhrf3)
    zhrf3 = re.sub('U', '𝐮', zhrf3)
    zhrf3 = re.sub('I', '𝐢', zhrf3)
    zhrf3 = re.sub('O', '𝐨', zhrf3)
    zhrf3 = re.sub('P', '𝐩', zhrf3)
    zhrf3 = re.sub('A', '𝐚', zhrf3)
    zhrf3 = re.sub('S', '𝐬', zhrf3)
    zhrf3 = re.sub('D', '𝐝', zhrf3)
    zhrf3 = re.sub('F', '𝐟', zhrf3)
    zhrf3 = re.sub('G', '𝐠', zhrf3)
    zhrf3 = re.sub('H', '𝐡', zhrf3)
    zhrf3 = re.sub('J', '𝐣', zhrf3)
    zhrf3 = re.sub('K', '𝐤', zhrf3)
    zhrf3 = re.sub('L', '𝐥', zhrf3)
    zhrf3 = re.sub('l', '𝐥', zhrf3)
    zhrf3 = re.sub('z', '𝐳', zhrf3)
    zhrf3 = re.sub('Z', '𝐳', zhrf3)
    zhrf3 = re.sub('x', '𝐱', zhrf3)
    zhrf3 = re.sub('X', 'ẋ', zhrf3)
    zhrf3 = re.sub('c', '𝐜', zhrf3)
    zhrf3 = re.sub('C', '𝐜', zhrf3)
    zhrf3 = re.sub('v', '𝐯', zhrf3)
    zhrf3 = re.sub('V', '𝐯', zhrf3)
    zhrf3 = re.sub('b', '𝐛', zhrf3)
    zhrf3 = re.sub('B', '𝐛', zhrf3)
    zhrf3 = re.sub('n', '𝐧', zhrf3)
    zhrf3 = re.sub('N', '𝐧', zhrf3)
    zhrf3 = re.sub('m', '𝐦', zhrf3)
    zhrf3 = re.sub('M', '𝐦', zhrf3)

    zhrf4 = re.sub('ض', 'ضۜہٰٰ', m.text)
    zhrf4 = re.sub('ص', 'ضۜہٰٰ', zhrf4)
    zhrf4 = re.sub('ث', 'ثہٰٰ', zhrf4)
    zhrf4 = re.sub('ق', 'قྀ̲ہٰٰ', zhrf4)
    zhrf4 = re.sub('ف', 'ف͒ہٰٰ', zhrf4)
    zhrf4 = re.sub('غ', 'غہٰٰ', zhrf4)
    zhrf4 = re.sub('ع', 'عہٰٰ', zhrf4)
    zhrf4 = re.sub('ه', 'هٰہٰٖ', zhrf4)
    zhrf4 = re.sub('خ', 'خٰ̐ہ ', zhrf4)
    zhrf4 = re.sub('ح', 'حہٰٰ', zhrf4)
    zhrf4 = re.sub('ج', 'جـٰ̲ـہْۧ', zhrf4)
    zhrf4 = re.sub('د', 'دٰ', zhrf4)
    zhrf4 = re.sub('ذ', 'ذِٰ', zhrf4)
    zhrf4 = re.sub('ش', 'شِٰہٰٰ', zhrf4)
    zhrf4 = re.sub('س', 'سٰٓ', zhrf4)
    zhrf4 = re.sub('ي', 'يِٰہ', zhrf4)
    zhrf4 = re.sub('ب', 'بّہ', zhrf4)
    zhrf4 = re.sub('ل', 'لـٰ̲ـہ', zhrf4)
    zhrf4 = re.sub('ا', 'آ', zhrf4)
    zhrf4 = re.sub('ت', 'تَہَٰ', zhrf4)
    zhrf4 = re.sub('ن', 'نَِہ', zhrf4)
    zhrf4 = re.sub('م', 'مٰ̲ہ', zhrf4)
    zhrf4 = re.sub('ك', 'ڪٰྀہٰٰ', zhrf4)
    zhrf4 = re.sub('ط', 'طۨہٰٰ', zhrf4)
    zhrf4 = re.sub('ئ', 'ئ ْٰ', zhrf4)
    zhrf4 = re.sub('ء', 'ء', zhrf4)
    zhrf4 = re.sub('ؤ', 'ؤ', zhrf4)
    zhrf4 = re.sub('ر', 'رَ', zhrf4)
    zhrf4 = re.sub('لا', 'لہا', zhrf4)
    zhrf4 = re.sub('ى', 'ىْ', zhrf4)
    zhrf4 = re.sub('ة', 'ة', zhrf4)
    zhrf4 = re.sub('و', 'وِٰ', zhrf4)
    zhrf4 = re.sub('ز', 'زَٰ', zhrf4)
    zhrf4 = re.sub('ظ', 'ظۗہٰٰ', zhrf4)
    zhrf4 = re.sub('q', '𝑸', zhrf4)
    zhrf4 = re.sub('Q', '𝑸', zhrf4)
    zhrf4 = re.sub('w', '𝑾', zhrf4)
    zhrf4 = re.sub('W', '𝑾', zhrf4)
    zhrf4 = re.sub('e', '𝑬', zhrf4)
    zhrf4 = re.sub('E', '𝑬', zhrf4)
    zhrf4 = re.sub('r', '𝑹', zhrf4)
    zhrf4 = re.sub('R', '𝑹', zhrf4)
    zhrf4 = re.sub('t', '𝑻', zhrf4)
    zhrf4 = re.sub('T', '𝑻', zhrf4)
    zhrf4 = re.sub('y', '𝒀', zhrf4)
    zhrf4 = re.sub('Y', '𝒀', zhrf4)
    zhrf4 = re.sub('u', '𝑼', zhrf4)
    zhrf4 = re.sub('U', '𝑼', zhrf4)
    zhrf4 = re.sub('i', '𝑰', zhrf4)
    zhrf4 = re.sub('I', '𝑰', zhrf4)
    zhrf4 = re.sub('o', '𝑶', zhrf4)
    zhrf4 = re.sub('O', '𝑶', zhrf4)
    zhrf4 = re.sub('p', '𝑷', zhrf4)
    zhrf4 = re.sub('P', '𝑷', zhrf4)
    zhrf4 = re.sub('a', '𝑨', zhrf4)
    zhrf4 = re.sub('A', '𝑨', zhrf4)
    zhrf4 = re.sub('s', '𝑺', zhrf4)
    zhrf4 = re.sub('S', '𝑺', zhrf4)
    zhrf4 = re.sub('d', '𝑫', zhrf4)
    zhrf4 = re.sub('D', '𝑫', zhrf4)
    zhrf4 = re.sub('f', '𝑭', zhrf4)
    zhrf4 = re.sub('F', '𝑭', zhrf4)
    zhrf4 = re.sub('g', '𝑮', zhrf4)
    zhrf4 = re.sub('G', '𝑮', zhrf4)
    zhrf4 = re.sub('h', '𝑯', zhrf4)
    zhrf4 = re.sub('H', '𝑯', zhrf4)
    zhrf4 = re.sub('j', '𝑱', zhrf4)
    zhrf4 = re.sub('J', '𝑱', zhrf4)
    zhrf4 = re.sub('k', '𝑲', zhrf4)
    zhrf4 = re.sub('K', '𝑲', zhrf4)
    zhrf4 = re.sub('l', '𝑳', zhrf4)
    zhrf4 = re.sub('L', '𝑳', zhrf4)
    zhrf4 = re.sub('z', '𝒁', zhrf4)
    zhrf4 = re.sub('Z', '𝒁', zhrf4)
    zhrf4 = re.sub('x', '𝑿', zhrf4)
    zhrf4 = re.sub('X', '𝑿', zhrf4)
    zhrf4 = re.sub('c', '𝑪', zhrf4)
    zhrf4 = re.sub('C', '𝑪', zhrf4)
    zhrf4 = re.sub('v', '𝑽', zhrf4)
    zhrf4 = re.sub('V', '𝑽', zhrf4)
    zhrf4 = re.sub('b', '𝑩', zhrf4)
    zhrf4 = re.sub('B', '𝑩', zhrf4)
    zhrf4 = re.sub('n', '𝑵', zhrf4)
    zhrf4 = re.sub('N', '𝑵', zhrf4)
    zhrf4 = re.sub('m', '𝑴', zhrf4)
    zhrf4 = re.sub('M', '𝑴', zhrf4)

    zhrf5 = re.sub('ض', 'ضَ', m.text)
    zhrf5 = re.sub('ص', 'صً', zhrf5)
    zhrf5 = re.sub('ث', 'ثَ', zhrf5)
    zhrf5 = re.sub('ق', 'قُ', zhrf5)
    zhrf5 = re.sub('ف', 'فّ', zhrf5)
    zhrf5 = re.sub('غ', 'غِ', zhrf5)
    zhrf5 = re.sub('ع', 'عُ', zhrf5)
    zhrf5 = re.sub('ه', 'ﮭ', zhrf5)
    zhrf5 = re.sub('خ', 'خِ', zhrf5)
    zhrf5 = re.sub('ح', 'حٌ', zhrf5)
    zhrf5 = re.sub('ج', 'جُ', zhrf5)
    zhrf5 = re.sub('د', 'دِ', zhrf5)
    zhrf5 = re.sub('ذ', 'ذَ', zhrf5)
    zhrf5 = re.sub('ش', 'شِ', zhrf5)
    zhrf5 = re.sub('س', 'سً', zhrf5)
    zhrf5 = re.sub('ي', 'يْ', zhrf5)
    zhrf5 = re.sub('ب', 'بّ', zhrf5)
    zhrf5 = re.sub('ل', 'لَ', zhrf5)
    zhrf5 = re.sub('ا', 'أُ', zhrf5)
    zhrf5 = re.sub('ت', 'تٌ', zhrf5)
    zhrf5 = re.sub('ن', 'نً', zhrf5)
    zhrf5 = re.sub('م', 'مِ', zhrf5)
    zhrf5 = re.sub('ك', 'ڳّ', zhrf5)
    zhrf5 = re.sub('ط', 'طٌ', zhrf5)
    zhrf5 = re.sub('ئ', 'ئ', zhrf5)
    zhrf5 = re.sub('ء', 'ء', zhrf5)
    zhrf5 = re.sub('ؤ', 'ؤ', zhrf5)
    zhrf5 = re.sub('ر', 'رٌ', zhrf5)
    zhrf5 = re.sub('لا', 'لٌأً', zhrf5)
    zhrf5 = re.sub('ى', 'ى', zhrf5)
    zhrf5 = re.sub('ة', 'ةَ', zhrf5)
    zhrf5 = re.sub('و', 'وِ', zhrf5)
    zhrf5 = re.sub('ز', 'زُ', zhrf5)
    zhrf5 = re.sub('ظ', 'ظ', zhrf5)
    zhrf5 = re.sub('q', '𝒒', zhrf5)
    zhrf5 = re.sub('Q', '𝒒', zhrf5)
    zhrf5 = re.sub('w', '𝒘', zhrf5)
    zhrf5 = re.sub('W', '𝒘', zhrf5)
    zhrf5 = re.sub('e', '𝒆', zhrf5)
    zhrf5 = re.sub('E', '𝒆', zhrf5)
    zhrf5 = re.sub('r', '𝒓', zhrf5)
    zhrf5 = re.sub('R', '𝒓', zhrf5)
    zhrf5 = re.sub('t', '𝒕', zhrf5)
    zhrf5 = re.sub('T', '𝒕', zhrf5)
    zhrf5 = re.sub('y', '𝒚', zhrf5)
    zhrf5 = re.sub('Y', '𝒚', zhrf5)
    zhrf5 = re.sub('u', '𝒖', zhrf5)
    zhrf5 = re.sub('U', '𝒖', zhrf5)
    zhrf5 = re.sub('i', '𝒊', zhrf5)
    zhrf5 = re.sub('I', '𝒊', zhrf5)
    zhrf5 = re.sub('o', '𝒐', zhrf5)
    zhrf5 = re.sub('O', '𝒐', zhrf5)
    zhrf5 = re.sub('p', '𝒑', zhrf5)
    zhrf5 = re.sub('P', '𝒑', zhrf5)
    zhrf5 = re.sub('a', '𝒂', zhrf5)
    zhrf5 = re.sub('A', '𝒂', zhrf5)
    zhrf5 = re.sub('s', '𝒔', zhrf5)
    zhrf5 = re.sub('S', '𝒔', zhrf5)
    zhrf5 = re.sub('d', '𝒅', zhrf5)
    zhrf5 = re.sub('D', '𝒅', zhrf5)
    zhrf5 = re.sub('f', '𝒇', zhrf5)
    zhrf5 = re.sub('F', '𝒇', zhrf5)
    zhrf5 = re.sub('g', '𝒈', zhrf5)
    zhrf5 = re.sub('G', '𝒈', zhrf5)
    zhrf5 = re.sub('h', '𝒉', zhrf5)
    zhrf5 = re.sub('H', '𝒉', zhrf5)
    zhrf5 = re.sub('j', '𝒋', zhrf5)
    zhrf5 = re.sub('J', '𝒋', zhrf5)
    zhrf5 = re.sub('K', '𝒌', zhrf5)
    zhrf5 = re.sub('k', '𝒌', zhrf5)
    zhrf5 = re.sub('L', '𝒍', zhrf5)
    zhrf5 = re.sub('l', '𝒍', zhrf5)
    zhrf5 = re.sub('z', '𝒛', zhrf5)
    zhrf5 = re.sub('Z', '𝒛', zhrf5)
    zhrf5 = re.sub('x', '𝒙', zhrf5)
    zhrf5 = re.sub('X', '𝒙', zhrf5)
    zhrf5 = re.sub('c', '𝒄', zhrf5)
    zhrf5 = re.sub('C', '𝒄', zhrf5)
    zhrf5 = re.sub('v', '𝒗', zhrf5)
    zhrf5 = re.sub('V', '𝒗', zhrf5)
    zhrf5 = re.sub('b', '𝒃', zhrf5)
    zhrf5 = re.sub('B', '𝒃', zhrf5)
    zhrf5 = re.sub('n', '𝒏', zhrf5)
    zhrf5 = re.sub('N', '𝒏', zhrf5)
    zhrf5 = re.sub('m', '𝒎', zhrf5)
    zhrf5 = re.sub('M', '𝒎', zhrf5)

    zhrf6 = re.sub('ض', 'ﺿ̭͠', m.text)
    zhrf6 = re.sub('ص', 'ﺻ͡', zhrf6)
    zhrf6 = re.sub('ث', 'ﺜ̲', zhrf6)
    zhrf6 = re.sub('ق', 'ﭰ', zhrf6)
    zhrf6 = re.sub('ف', 'ﻓ̲', zhrf6)
    zhrf6 = re.sub('غ', 'ﻏ̲', zhrf6)
    zhrf6 = re.sub('ع', 'ﻌ̲', zhrf6)
    zhrf6 = re.sub('ه', 'ﮬ̲̌', zhrf6)
    zhrf6 = re.sub('خ', 'خٌ', zhrf6)
    zhrf6 = re.sub('ح', 'ﺣ̅', zhrf6)
    zhrf6 = re.sub('ج', 'جُ', zhrf6)
    zhrf6 = re.sub('د', 'ډ̝', zhrf6)
    zhrf6 = re.sub('ذ', 'ذً', zhrf6)
    zhrf6 = re.sub('ش', 'ﺷ̲', zhrf6)
    zhrf6 = re.sub('س', 'ﺳ̉', zhrf6)
    zhrf6 = re.sub('ي', 'ﯾ̃̐', zhrf6)
    zhrf6 = re.sub('ب', 'ﺑ̲', zhrf6)
    zhrf6 = re.sub('ل', 'ا̄ﻟ', zhrf6)
    zhrf6 = re.sub('ا', 'ﺈ̃', zhrf6)
    zhrf6 = re.sub('ت', 'ټُ', zhrf6)
    zhrf6 = re.sub('ن', 'ﻧ̲', zhrf6)
    zhrf6 = re.sub('م', 'ﻣ̲̉', zhrf6)
    zhrf6 = re.sub('ك', 'گ', zhrf6)
    zhrf6 = re.sub('ط', 'ﻁ̲', zhrf6)
    zhrf6 = re.sub('ئ', ' ْٰئ', zhrf6)
    zhrf6 = re.sub('ء', 'ء', zhrf6)
    zhrf6 = re.sub('ؤ', 'ؤ', zhrf6)
    zhrf6 = re.sub('ر', 'ہڕ', zhrf6)
    zhrf6 = re.sub('لا', 'ﻟ̲ﺂ̲', zhrf6)
    zhrf6 = re.sub('ى', 'ى', zhrf6)
    zhrf6 = re.sub('ة', 'ة', zhrf6)
    zhrf6 = re.sub('و', 'ۇۈۉ', zhrf6)
    zhrf6 = re.sub('ز', 'زُ', zhrf6)
    zhrf6 = re.sub('ظ', 'ﻇ̲', zhrf6)
    zhrf6 = re.sub('q', 'ǫ', zhrf6)
    zhrf6 = re.sub('Q', 'ǫ', zhrf6)
    zhrf6 = re.sub('w', 'ᴡ', zhrf6)
    zhrf6 = re.sub('W', 'ᴡ', zhrf6)
    zhrf6 = re.sub('e', 'ᴇ', zhrf6)
    zhrf6 = re.sub('E', 'ᴇ', zhrf6)
    zhrf6 = re.sub('r', 'ʀ', zhrf6)
    zhrf6 = re.sub('R', 'ʀ', zhrf6)
    zhrf6 = re.sub('t', 'ᴛ', zhrf6)
    zhrf6 = re.sub('T', 'ᴛ', zhrf6)
    zhrf6 = re.sub('y', 'ʏ', zhrf6)
    zhrf6 = re.sub('Y', 'ʏ', zhrf6)
    zhrf6 = re.sub('u', 'ụ', zhrf6)
    zhrf6 = re.sub('U', 'ụ', zhrf6)
    zhrf6 = re.sub('i', 'ɪ', zhrf6)
    zhrf6 = re.sub('I', 'ɪ', zhrf6)
    zhrf6 = re.sub('o', 'ᴏ', zhrf6)
    zhrf6 = re.sub('O', 'ᴏ', zhrf6)
    zhrf6 = re.sub('p', 'ᴘ', zhrf6)
    zhrf6 = re.sub('P', 'ᴘ', zhrf6)
    zhrf6 = re.sub('a', 'ᴀ', zhrf6)
    zhrf6 = re.sub('A', 'ᴀ', zhrf6)
    zhrf6 = re.sub('s', 'ѕ', zhrf6)
    zhrf6 = re.sub('S', 'ѕ', zhrf6)
    zhrf6 = re.sub('d', 'ᴅ', zhrf6)
    zhrf6 = re.sub('D', 'ᴅ', zhrf6)
    zhrf6 = re.sub('f', 'ғ', zhrf6)
    zhrf6 = re.sub('F', 'ғ', zhrf6)
    zhrf6 = re.sub('g', 'ɢ', zhrf6)
    zhrf6 = re.sub('G', 'ɢ', zhrf6)
    zhrf6 = re.sub('h', 'ʜ', zhrf6)
    zhrf6 = re.sub('H', 'ʜ', zhrf6)
    zhrf6 = re.sub('j', 'ᴊ', zhrf6)
    zhrf6 = re.sub('J', 'ᴊ', zhrf6)
    zhrf6 = re.sub('K', 'ᴋ', zhrf6)
    zhrf6 = re.sub('k', 'ᴋ', zhrf6)
    zhrf6 = re.sub('L', 'ʟ', zhrf6)
    zhrf6 = re.sub('l', 'ʟ', zhrf6)
    zhrf6 = re.sub('z', 'ᴢ', zhrf6)
    zhrf6 = re.sub('Z', 'ᴢ', zhrf6)
    zhrf6 = re.sub('x', 'х', zhrf6)
    zhrf6 = re.sub('X', 'х', zhrf6)
    zhrf6 = re.sub('c', 'ᴄ', zhrf6)
    zhrf6 = re.sub('C', 'ᴄ', zhrf6)
    zhrf6 = re.sub('v', 'ᴠ', zhrf6)
    zhrf6 = re.sub('V', 'ᴠ', zhrf6)
    zhrf6 = re.sub('b', 'ʙ', zhrf6)
    zhrf6 = re.sub('B', 'ʙ', zhrf6)
    zhrf6 = re.sub('n', 'ɴ', zhrf6)
    zhrf6 = re.sub('N', 'ɴ', zhrf6)
    zhrf6 = re.sub('m', 'ᴍ', zhrf6)
    zhrf6 = re.sub('M', 'ᴍ', zhrf6)

    zhrf7 = re.sub('ض', 'ﺿ', m.text)
    zhrf7 = re.sub('ص', 'ﺻ', zhrf7)
    zhrf7 = re.sub('ث', 'ﭥ', zhrf7)
    zhrf7 = re.sub('ق', 'ﻗ̮ـ̃', zhrf7)
    zhrf7 = re.sub('ف', 'ﭬ', zhrf7)
    zhrf7 = re.sub('غ', 'ﻏ̣̐', zhrf7)
    zhrf7 = re.sub('ع', 'ﻋ', zhrf7)
    zhrf7 = re.sub('ه', 'ھَہّ', zhrf7)
    zhrf7 = re.sub('خ', 'ﺧ', zhrf7)
    zhrf7 = re.sub('ح', 'פ', zhrf7)
    zhrf7 = re.sub('ج', 'ﭴ', zhrf7)
    zhrf7 = re.sub('د', 'ﮃ', zhrf7)
    zhrf7 = re.sub('ذ', 'ذ', zhrf7)
    zhrf7 = re.sub('ش', 'ﺷ', zhrf7)
    zhrf7 = re.sub('س', 'ﺳ', zhrf7)
    zhrf7 = re.sub('ي', 'ﯾ', zhrf7)
    zhrf7 = re.sub('ب', 'ﺑ', zhrf7)
    zhrf7 = re.sub('ل', 'ﻟ', zhrf7)
    zhrf7 = re.sub('ا', 'ﺂ', zhrf7)
    zhrf7 = re.sub('ت', 'ﭠ', zhrf7)
    zhrf7 = re.sub('ن', 'ﻧ', zhrf7)
    zhrf7 = re.sub('م', 'ﻣ̝̚', zhrf7)
    zhrf7 = re.sub('ك', 'گـ', zhrf7)
    zhrf7 = re.sub('ط', 'ﻁْ', zhrf7)
    zhrf7 = re.sub('ئ', 'ٰئـ', zhrf7)
    zhrf7 = re.sub('ء', 'ء', zhrf7)
    zhrf7 = re.sub('ؤ', 'ﯗ', zhrf7)
    zhrf7 = re.sub('ر', 'ړُ', zhrf7)
    zhrf7 = re.sub('لا', 'ﻟآ', zhrf7)
    zhrf7 = re.sub('ى', 'ـﮯ', zhrf7)
    zhrf7 = re.sub('ة', 'ة', zhrf7)
    zhrf7 = re.sub('و', 'ۆ', zhrf7)
    zhrf7 = re.sub('ز', 'ژ', zhrf7)
    zhrf7 = re.sub('ظ', 'ﻅ', zhrf7)
    zhrf7 = re.sub('q', '𝘘', zhrf7)
    zhrf7 = re.sub('Q', '𝘘', zhrf7)
    zhrf7 = re.sub('w', '𝘞', zhrf7)
    zhrf7 = re.sub('W', '𝘞', zhrf7)
    zhrf7 = re.sub('e', '𝘌', zhrf7)
    zhrf7 = re.sub('E', '𝘌', zhrf7)
    zhrf7 = re.sub('r', '𝘙', zhrf7)
    zhrf7 = re.sub('R', '𝘙', zhrf7)
    zhrf7 = re.sub('t', '𝘛', zhrf7)
    zhrf7 = re.sub('T', '𝘛', zhrf7)
    zhrf7 = re.sub('y', '𝘠', zhrf7)
    zhrf7 = re.sub('Y', '𝘠', zhrf7)
    zhrf7 = re.sub('u', '𝘜', zhrf7)
    zhrf7 = re.sub('U', '𝘜', zhrf7)
    zhrf7 = re.sub('i', '𝘐', zhrf7)
    zhrf7 = re.sub('I', '𝘐', zhrf7)
    zhrf7 = re.sub('o', '𝘖', zhrf7)
    zhrf7 = re.sub('O', '𝘖', zhrf7)
    zhrf7 = re.sub('p', '𝘗', zhrf7)
    zhrf7 = re.sub('P', '𝘗', zhrf7)
    zhrf7 = re.sub('a', '𝘈', zhrf7)
    zhrf7 = re.sub('A', '𝘈', zhrf7)
    zhrf7 = re.sub('s', '𝘚', zhrf7)
    zhrf7 = re.sub('S', '𝘚', zhrf7)
    zhrf7 = re.sub('d', '𝘋', zhrf7)
    zhrf7 = re.sub('D', '𝘋', zhrf7)
    zhrf7 = re.sub('f', '𝘍', zhrf7)
    zhrf7 = re.sub('F', '𝘍', zhrf7)
    zhrf7 = re.sub('g', '𝘎', zhrf7)
    zhrf7 = re.sub('G', '𝘎', zhrf7)
    zhrf7 = re.sub('h', '𝘏', zhrf7)
    zhrf7 = re.sub('H', '𝘏', zhrf7)
    zhrf7 = re.sub('j', '𝘑', zhrf7)
    zhrf7 = re.sub('J', '𝘑', zhrf7)
    zhrf7 = re.sub('k', '𝘒', zhrf7)
    zhrf7 = re.sub('K', '𝘒', zhrf7)
    zhrf7 = re.sub('L', '𝘓', zhrf7)
    zhrf7 = re.sub('l', '𝘓', zhrf7)
    zhrf7 = re.sub('z', '𝘡', zhrf7)
    zhrf7 = re.sub('Z', '𝘡', zhrf7)
    zhrf7 = re.sub('x', '𝘟', zhrf7)
    zhrf7 = re.sub('X', '𝘟', zhrf7)
    zhrf7 = re.sub('c', '𝘊', zhrf7)
    zhrf7 = re.sub('C', '𝘊', zhrf7)
    zhrf7 = re.sub('v', '𝘝', zhrf7)
    zhrf7 = re.sub('V', '𝘝', zhrf7)
    zhrf7 = re.sub('b', '𝘉', zhrf7)
    zhrf7 = re.sub('B', '𝘉', zhrf7)
    zhrf7 = re.sub('n', '𝘕', zhrf7)
    zhrf7 = re.sub('N', '𝘕', zhrf7)
    zhrf7 = re.sub('m', '𝘔', zhrf7)
    zhrf7 = re.sub('M', '𝘔', zhrf7)

    zhrf8 = re.sub('ض', 'ض', m.text)
    zhrf8 = re.sub('ص', 'صہٰ', zhrf8)
    zhrf8 = re.sub('ث', 'ثہٰـ', zhrf8)
    zhrf8 = re.sub('ق', 'قہٰ', zhrf8)
    zhrf8 = re.sub('ف', 'فہٰ', zhrf8)
    zhrf8 = re.sub('غ', 'غـْ', zhrf8)
    zhrf8 = re.sub('ع', 'ع', zhrf8)
    zhrf8 = re.sub('ه', 'هٰہٰٖ', zhrf8)
    zhrf8 = re.sub('خ', 'خخَـ', zhrf8)
    zhrf8 = re.sub('ح', 'حہٰ', zhrf8)
    zhrf8 = re.sub('ج', 'ججہٰ', zhrf8)
    zhrf8 = re.sub('د', 'دَ', zhrf8)
    zhrf8 = re.sub('ذ', 'ذّ', zhrf8)
    zhrf8 = re.sub('ش', 'ششہٰ', zhrf8)
    zhrf8 = re.sub('س', 'سہٰ', zhrf8)
    zhrf8 = re.sub('ي', 'يٰ', zhrf8)
    zhrf8 = re.sub('ب', 'بٰٰ', zhrf8)
    zhrf8 = re.sub('ل', 'لہٰ', zhrf8)
    zhrf8 = re.sub('ا', 'آ', zhrf8)
    zhrf8 = re.sub('ت', 'تہٰ', zhrf8)
    zhrf8 = re.sub('ن', 'نہٰ', zhrf8)
    zhrf8 = re.sub('م', 'مہٰ', zhrf8)
    zhrf8 = re.sub('ك', 'ككہٰ', zhrf8)
    zhrf8 = re.sub('ط', 'طہٰ', zhrf8)
    zhrf8 = re.sub('ئ', ' ْئٰ', zhrf8)
    zhrf8 = re.sub('ء', 'ء', zhrf8)
    zhrf8 = re.sub('ؤ', 'ؤؤَ', zhrf8)
    zhrf8 = re.sub('ر', 'رَ', zhrf8)
    zhrf8 = re.sub('لا', 'لہٰا', zhrf8)
    zhrf8 = re.sub('ى', 'ىہٰ', zhrf8)
    zhrf8 = re.sub('ة', 'ة', zhrf8)
    zhrf8 = re.sub('و', 'ہٰو', zhrf8)
    zhrf8 = re.sub('ز', 'ز', zhrf8)
    zhrf8 = re.sub('ظ', 'ظہٰ', zhrf8)
    zhrf8 = re.sub('q', '𝚀', zhrf8)
    zhrf8 = re.sub('Q', '𝚀', zhrf8)
    zhrf8 = re.sub('w', '𝚆', zhrf8)
    zhrf8 = re.sub('W', '𝚆', zhrf8)
    zhrf8 = re.sub('e', '𝙴', zhrf8)
    zhrf8 = re.sub('E', '𝙴', zhrf8)
    zhrf8 = re.sub('r', '𝚁', zhrf8)
    zhrf8 = re.sub('R', '𝚁', zhrf8)
    zhrf8 = re.sub('t', '𝚃', zhrf8)
    zhrf8 = re.sub('T', '𝚃', zhrf8)
    zhrf8 = re.sub('y', '𝚈', zhrf8)
    zhrf8 = re.sub('Y', '𝚈', zhrf8)
    zhrf8 = re.sub('u', '𝚄', zhrf8)
    zhrf8 = re.sub('U', '𝚄', zhrf8)
    zhrf8 = re.sub('i', '𝙸', zhrf8)
    zhrf8 = re.sub('I', '𝙸', zhrf8)
    zhrf8 = re.sub('o', '𝙾', zhrf8)
    zhrf8 = re.sub('O', '𝙾', zhrf8)
    zhrf8 = re.sub('p', '𝙿', zhrf8)
    zhrf8 = re.sub('P', '𝙿', zhrf8)
    zhrf8 = re.sub('a', '𝙰', zhrf8)
    zhrf8 = re.sub('A', '𝙰', zhrf8)
    zhrf8 = re.sub('s', '𝚂', zhrf8)
    zhrf8 = re.sub('S', '𝚂', zhrf8)
    zhrf8 = re.sub('d', '𝙳', zhrf8)
    zhrf8 = re.sub('D', '𝙳', zhrf8)
    zhrf8 = re.sub('f', '𝙵', zhrf8)
    zhrf8 = re.sub('F', '𝙵', zhrf8)
    zhrf8 = re.sub('g', '𝙶', zhrf8)
    zhrf8 = re.sub('G', '𝙶', zhrf8)
    zhrf8 = re.sub('h', '𝙷', zhrf8)
    zhrf8 = re.sub('H', '𝙷', zhrf8)
    zhrf8 = re.sub('j', '𝙹', zhrf8)
    zhrf8 = re.sub('J', '𝙹', zhrf8)
    zhrf8 = re.sub('k', '𝙺', zhrf8)
    zhrf8 = re.sub('K', '𝙺', zhrf8)
    zhrf8 = re.sub('L', '𝙻', zhrf8)
    zhrf8 = re.sub('l', '𝙻', zhrf8)
    zhrf8 = re.sub('z', '𝚉', zhrf8)
    zhrf8 = re.sub('Z', '𝚉', zhrf8)
    zhrf8 = re.sub('x', '𝚇', zhrf8)
    zhrf8 = re.sub('X', '𝚇', zhrf8)
    zhrf8 = re.sub('c', '𝙲', zhrf8)
    zhrf8 = re.sub('C', '𝙲', zhrf8)
    zhrf8 = re.sub('v', '𝚅', zhrf8)
    zhrf8 = re.sub('V', '𝚅', zhrf8)
    zhrf8 = re.sub('b', '𝙱', zhrf8)
    zhrf8 = re.sub('B', '𝙱', zhrf8)
    zhrf8 = re.sub('n', '𝙽', zhrf8)
    zhrf8 = re.sub('N', '𝙽', zhrf8)
    zhrf8 = re.sub('m', '𝙼', zhrf8)
    zhrf8 = re.sub('M', '𝙼', zhrf8)

    zhrf9 = re.sub('ض', 'ض', m.text)
    zhrf9 = re.sub('ص', 'ص', zhrf9)
    zhrf9 = re.sub('ث', 'ث', zhrf9)
    zhrf9 = re.sub('ق', 'قٌ', zhrf9)
    zhrf9 = re.sub('ف', 'فُ', zhrf9)
    zhrf9 = re.sub('غ', 'غ', zhrf9)
    zhrf9 = re.sub('ع', 'عٍ', zhrf9)
    zhrf9 = re.sub('ه', 'هـ', zhrf9)
    zhrf9 = re.sub('خ', 'خـ', zhrf9)
    zhrf9 = re.sub('ح', 'حٍ', zhrf9)
    zhrf9 = re.sub('ج', 'جٍ', zhrf9)
    zhrf9 = re.sub('د', 'دِ', zhrf9)
    zhrf9 = re.sub('ذ', 'ذَ', zhrf9)
    zhrf9 = re.sub('ش', 'شُ', zhrf9)
    zhrf9 = re.sub('س', 'س', zhrf9)
    zhrf9 = re.sub('ي', 'ي', zhrf9)
    zhrf9 = re.sub('ب', 'بَ', zhrf9)
    zhrf9 = re.sub('ل', 'لُِ', zhrf9)
    zhrf9 = re.sub('ا', 'آ', zhrf9)
    zhrf9 = re.sub('ت', 'ت', zhrf9)
    zhrf9 = re.sub('ن', 'ن', zhrf9)
    zhrf9 = re.sub('م', 'م', zhrf9)
    zhrf9 = re.sub('ك', 'ڪ', zhrf9)
    zhrf9 = re.sub('ط', 'طُ', zhrf9)
    zhrf9 = re.sub('ئ', 'ئ ْٰ', zhrf9)
    zhrf9 = re.sub('ء', 'ء', zhrf9)
    zhrf9 = re.sub('ؤ', 'ؤ', zhrf9)
    zhrf9 = re.sub('ر', 'ر', zhrf9)
    zhrf9 = re.sub('لا', 'لُِآ', zhrf9)
    zhrf9 = re.sub('ى', 'ىْ', zhrf9)
    zhrf9 = re.sub('ة', 'ة', zhrf9)
    zhrf9 = re.sub('و', 'وو', zhrf9)
    zhrf9 = re.sub('ز', 'ز', zhrf9)
    zhrf9 = re.sub('ظ', 'ظهُ', zhrf9)
    zhrf9 = re.sub('q', 'ℚ', zhrf9)
    zhrf9 = re.sub('Q', 'ℚ', zhrf9)
    zhrf9 = re.sub('w', '𝕎', zhrf9)
    zhrf9 = re.sub('W', '𝕎', zhrf9)
    zhrf9 = re.sub('e', '𝔼', zhrf9)
    zhrf9 = re.sub('E', '𝔼', zhrf9)
    zhrf9 = re.sub('r', 'ℝ', zhrf9)
    zhrf9 = re.sub('R', 'ℝ', zhrf9)
    zhrf9 = re.sub('t', '𝕋', zhrf9)
    zhrf9 = re.sub('T', '𝕋', zhrf9)
    zhrf9 = re.sub('y', '𝕐', zhrf9)
    zhrf9 = re.sub('Y', '𝕐', zhrf9)
    zhrf9 = re.sub('u', '𝕌', zhrf9)
    zhrf9 = re.sub('U', '𝕌', zhrf9)
    zhrf9 = re.sub('i', '𝕀', zhrf9)
    zhrf9 = re.sub('I', '𝕀', zhrf9)
    zhrf9 = re.sub('o', '𝕆', zhrf9)
    zhrf9 = re.sub('O', '𝕆', zhrf9)
    zhrf9 = re.sub('p', 'ℙ', zhrf9)
    zhrf9 = re.sub('P', 'ℙ', zhrf9)
    zhrf9 = re.sub('a', '𝔸', zhrf9)
    zhrf9 = re.sub('A', '𝔸', zhrf9)
    zhrf9 = re.sub('s', '𝕊', zhrf9)
    zhrf9 = re.sub('S', '𝕊', zhrf9)
    zhrf9 = re.sub('d', '𝔻', zhrf9)
    zhrf9 = re.sub('D', '𝔻', zhrf9)
    zhrf9 = re.sub('f', '𝔽', zhrf9)
    zhrf9 = re.sub('F', '𝔽', zhrf9)
    zhrf9 = re.sub('g', '𝔾', zhrf9)
    zhrf9 = re.sub('G', '𝔾', zhrf9)
    zhrf9 = re.sub('h', 'ℍ', zhrf9)
    zhrf9 = re.sub('H', 'ℍ', zhrf9)
    zhrf9 = re.sub('j', '𝕁', zhrf9)
    zhrf9 = re.sub('J', '𝕁', zhrf9)
    zhrf9 = re.sub('k', '𝕂', zhrf9)
    zhrf9 = re.sub('K', '𝕂', zhrf9)
    zhrf9 = re.sub('L', '𝕃', zhrf9)
    zhrf9 = re.sub('l', '𝕃', zhrf9)
    zhrf9 = re.sub('z', 'ℤ', zhrf9)
    zhrf9 = re.sub('Z', 'ℤ', zhrf9)
    zhrf9 = re.sub('x', '𝕏', zhrf9)
    zhrf9 = re.sub('X', '𝕏', zhrf9)
    zhrf9 = re.sub('c', 'ℂ', zhrf9)
    zhrf9 = re.sub('C', 'ℂ', zhrf9)
    zhrf9 = re.sub('v', '𝕍', zhrf9)
    zhrf9 = re.sub('V', '𝕍', zhrf9)
    zhrf9 = re.sub('b', '𝔹', zhrf9)
    zhrf9 = re.sub('B', '𝔹', zhrf9)
    zhrf9 = re.sub('n', 'ℕ', zhrf9)
    zhrf9 = re.sub('N', 'ℕ', zhrf9)
    zhrf9 = re.sub('m', '𝕄', zhrf9)
    zhrf9 = re.sub('M', '𝕄', zhrf9)

    Text_Zhrfa = "♕ `" + zhrf + random.choice(EmojeS) \
                 + "`\n\n` " + zhrf2 + random.choice(EmojeS) \
                 + "`\n\n` " + zhrf3 + random.choice(EmojeS) \
                 + "•\n\n` " + zhrf4 + random.choice(EmojeS) \
                 + "`\n\n` " + zhrf5 + random.choice(EmojeS) \
                 + "`\n\n` " + zhrf6 + random.choice(EmojeS) \
                 + "`\n\n` " + zhrf7 + random.choice(EmojeS) \
                 + "`\n\n` " + zhrf8 + random.choice(Emoje) \
                 + "`\n\n` " + zhrf9 + random.choice(Emoje) \
                 + "`\n\n` " + zhrf5 + random.choice(Emoje)
    Text_Zhrfa = Text_Zhrfa + "**\n\n دەست بدە لەناوەکە کۆپی دەبێت \n│ \n👾**"
    await m.reply_text(Text_Zhrfa, reply_to_message_id=m.id)
