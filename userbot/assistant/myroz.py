# @Jmthon - < https://t.me/Jmthon >
# Copyright (C) 2021 - JMTHON-AR
# All rights reserved.
#
# This file is a part of < https://github.com/JMTHON-AR/JMTHON >
# Please read the GNU Affero General Public License in;
# < https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE
# ===============================================================
#    جميع الحقوق لمطوري سورس سيلفا برو حصريا لهم فقط
#    اذا تخمط الملف اذك الحقوق وكاتبيه ومطوريه لا تحذف الحقوق وتصير فاشل 👍
#    كتابة محمد الزهيري
import re

from telethon import *
from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest

from Jmthon.razan.resources.assistant import *

# Telegram  :  @Jmthon  - @ttccss   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE
from userbot import bot
from userbot.sql_helper.idadder_sql import add_usersid_in_db, already_added

# Telegram  :  @Jmthon  - @ttccss   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE
from . import *


# start
@tgbot.on(events.NewMessage(pattern="^/start"))
async def start(event):
    razan = await tgbot.get_me()
    razan.first_name
    razan.username
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    vent = event.chat_id
    starttext = f"**مـرحبا {firstname} \n\n- [مـالك البـوت](tg://user?id={bot.uid}) \nيمكـنك مراسلـة المـالك عبـر هذا البـوت . \n\nاذا كـنت تـريد تنـصيب بـوت خـاص بـك تـاكد من الازرار بالأسفل**"
    if event.sender_id == bot.uid:
        await tgbot.send_message(
            vent,
            message=f"**اهلا بك مطـوري 🤍**\n**اختر احد الاوامر في الاسفل**\n\n**𓄼•𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐄𝐋𝐕𝐀•𓄹**\n𝙅dev SezR 🧸♥",
            buttons=[
                [
                    Button.url("• المطـور •", "https://t.me/ttccss"),
                    Button.inline("• لوحة التحكم •", data="gibcmd"),
                ],
                [
                    Button.inline("• اوامر البوت •", data="adrz"),
                ],
            ],
        )
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
        await tgbot.send_message(
            event.chat_id,
            message=starttext,
            link_preview=False,
            buttons=[
                [custom.Button.inline("• تنصيب سيلفا برو •", data="deploy")],
                [Button.url("• المساعدة  •", "https://t.me/br_selva")],
            ],
        )


# Data

# Telegram  :  @Jmthon  - @ttccss   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deploy")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message="**لو عايز تنصب علي سورس سيلفا بروو تواصل مع المطورين 🧸♥**.",
            buttons=[
                [Button.url("المبرمج سيزر", "https://t.me/ttccss")],
                [Button.url("المبرمج تيمو", "https://t.me/tt_tt_4")],
            ],
        )


# Telegram  :  @Jmthon  - @ttccss   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE


# Telegram  :  @Jmthon  - @ttccss   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gibcmd")))
async def users(event):
    await event.delete()
    rorza = "**▾∮ قائـمه اوامر المطور **\n* تستخدم في ↫ `{botusername} ` فقط! `\n**𓄼•𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐄𝐋𝐕𝐀•𓄹**\n\n*الامر  ( اذاعة  ) \n- لعمل اذاعة لمستخدمي البوت ◛ ↶\n**⋆ قم بالرد ع الرسالة لاذاعتها للمستخدمين ↸**\n\n*الامر ( معلومات ) \n- لمعرفة الملصقات المرسلة ↶\n**⋆ بالرد ع المستخدم لجلب معلوماتة **\n\n*الامر ( حظر + سبب )\n- لحظر مستخدم من البوت \n**⋆ بالرد ع المستخدم مع سبب مثل **\n**حظر @RR9R7 قمت بازعاجي**\n\n* الامر ( الغاء حظر ) \n لالغاء حظر المستخدم من البوت √\n**⋆ الامر والمعرف والسبب (اختياري) مثل **\n**الغاء حظر @RR9R7 + السبب اختياري**\n\n**⋆ الامر ( المحظورين )\n- لمعرفة المحظورين من البوت  **\n\n**⋆ امر ( المستخدمين ) \n- لمعرفة مستخدمين بوتك  **\n\n**⋆ الاوامر ( التكرار + تفعيل / تعطيل ) \n- تشغيل وايقاف التكرار (في البوت) ↶**\n* عند التشغيل يحظر المزعجين تلقائيًا ⊝\n\n\n**𓄼•𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐄𝐋𝐕𝐀•𓄹**\n𝙅𝙈𝙏𝙃𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 🧸♥"
    await tgbot.send_message(event.chat_id, rorza)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"jm_hhack")))
async def users(event):
    await event.delete()
    rorza = "تستطيع اختراق اي شخص عبر كود تيرمكس في سيلفا برو يمكنك اختراق المستخدمين الذي تملك كود تيرمكس الخاص بهم \n\n ارسل  /rz للعرض الاوأمر"
    await tgbot.send_message(event.chat_id, rorza)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"adrz")))
async def users(event):
    await event.delete()
    rorza = "**▾∮ قائـمه اوامر البوت كحـماية المجموعه \n* تستخدم في المجموعات التي يكون فيها البوت مشرف\n𓄼•𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐄𝐋𝐕𝐀•𓄹\n\n*  (  /id  ) \n- لجلب ايدي الدردشة او ايدي المستخدم ◛ ↶\n⋆ قم بالرد على المستخدم لجلب الايدي ↸\n\n*  ( /alive ) \n- للتأكد من حالة البوت فقط ↶\n⋆ فقط ارسل الامر\n\n*  (  /purge  )\n- لمسح رسائل الدردشة \n⋆ بالرد ع الرسالة البوت راح يمسح التحتها\n\n*  (  /del  ) \n-  لمسح رساله معينه\n⋆ قم بالرد على الرساله لمسحها \n\n𓄼•𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐄𝐋𝐕𝐀•𓄹\n𝙅𝙈𝙏𝙃𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 🧸♥"
    await tgbot.send_message(event.chat_id, rorza)


# Telegram  :  @Jmthon  - @ttccss   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE


@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def starkislub(event):
    razan = "**𓄼•𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐄𝐋𝐕𝐀•𓄹**\n•━═━═━═━═━━═━═━═━═━•‌‌\n**- حالة البوت **  يعمـل بنجـاح\n**- اصدار سيلفــا بــروو  **: 5.0.0\n**- اصدار البايثون **: 3.9.6\n**- يوزرك **\n**- CH : @SU_SELVA**\n\n"
    await event.reply(razan)


""" Telegram  :  @Jmthon  - @ttccss   -  https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE  """
"""  حقوقي شرفك تغير شي تلعب بشرفك """

# بـسـم الله الـرحمن الـرحيم  🤍
