from sys import version_info
from handlers import __version__
from pyrogram import Client, filters, __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from helpers.dbchat import add_served_chat, is_served_chat
from helpers.dbpunish import is_gbanned_user
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from time import time
from datetime import datetime

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    SUPPORT_GROUP,
    OWNER_NAME,
    UPDATES_CHANNEL,
    ASSISTANT_NAME,
    START_IMAGE, 
)
from helpers.filters import command, other_filters2
#  


__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)



@Client.on_message(filters.private & filters.incoming & filters.command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                f"{START_IMAGE}",
                caption=(f"""● **𝖬𝖾𝗋𝗁𝖺𝖻𝖺** {message.from_user.mention} \n\n● **𝖡𝖾𝗇** {BOT_NAME}!\n\n● **𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻𝖾𝗍𝗅𝖾𝗋𝖽𝖾 müzik 𝖢𝖺𝗅𝖺𝖻𝗂𝗅𝖾𝗇 𝖡𝗈𝗍𝗎𝗆 . . !** \n\n● **𝖡𝖺𝗇 𝖸𝖾𝗍𝗄𝗂𝗌𝗂𝗓, 𝖲𝖾𝗌 𝖸𝗈𝗇𝖾𝗍𝗂𝗆 𝖸𝖾𝗍𝗄𝗂𝗌𝗂 𝗏𝖾𝗋𝗂𝗉 𝖠𝗌𝗂𝗌𝗍𝖺𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾𝗒𝗂𝗇 . . !**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎉 𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾 🎉", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋", callback_data= "admin"
                    ),
                    InlineKeyboardButton(
                        "🇹🇷 𝖢𝗁𝖺𝗇𝗇𝖾𝗅", url="https://t.me/StarBotKanal"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧑🏻‍💻 ɢɪᴛʜᴜʙ ᴋᴀʏɴᴀᴋ ᴋᴏᴅᴜ 🧑🏻‍💻", url="https://github.com/MehmetAtes21/music"
                    )
                ]
                
           ]
        ),
    )

@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>🇹🇷 Tüm Komutlar : \n\n» /vbul => ᴠɪᴅᴇᴏ ɪɴᴅɪʀ . \n» /bul => ᴍᴜᴢɪᴋ ɪɴᴅɪʀ . \n» /oynat => ᴍᴜᴢɪᴋ ᴏʏɴᴀᴛ . \n» /durdur => ᴍᴜᴢɪɢɪ ᴅᴜʀᴅᴜʀ . \n» /devam => ᴍᴜᴢɪɢɪ sᴜʀᴅᴜʀ . \n» /atla =>  ᴍᴜᴢɪɢɪ ᴀᴛʟᴀ . \n» /son => ᴍᴜᴢɪɢɪ sᴏɴʟᴀɴᴅɪʀ . \n» /katil => ᴀsɪsᴛᴀɴɪ ɢʀᴜʙᴀ ᴅᴀᴠᴇᴛ ᴇᴅᴇʀ . \n» /reload => ᴀᴅᴍɪɴ ʟɪsᴛᴇsɪɴɪ ɢᴜɴᴄᴇʟʟᴇʀ . \n\n» /auth => ᴋᴜʟʟᴀɴɪᴄɪɴɪɴ ʏᴏɴᴇᴛɪᴄɪ ᴏʟᴍᴀᴅɪɢɪ ʜᴀʟᴅᴇ ᴋᴏᴍᴜᴛʟᴀʀɪ ᴋᴜʟʟᴀɴᴍᴀsɪɴᴀ ɪᴢɪɴ ᴠᴇʀɪʀ . \n\n» /unauth => ᴋᴜʟʟᴀɴɪᴄɪɴɪɴ ʏᴏɴᴇᴛɪᴄɪ ᴏʟᴍᴀᴅɪɢɪ ʜᴀʟᴅᴇ ᴋᴏᴍᴜᴛʟᴀʀɪ ᴋᴜʟʟᴀɴᴍᴀsɪɴɪ ᴇɴɢᴇʟʟᴇʀ . </b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🇹🇷 𝖠𝗌𝗂𝗌𝗍𝖺𝗇", url="https://t.me/StarMuzikAsistan"
                     ),
                     InlineKeyboardButton(
                         "🧑🏻‍💻 𝖮𝗐𝗇𝖾𝗋", url="https://t.me/Hayiboo"
                     )
                 ],
                 [
                     InlineKeyboardButton(
                         "✍🏻 𝖲𝖺𝗁𝗂𝗉 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋𝗂", callback_data ="sudo"
                     )
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ 𝖦𝖾𝗋𝗂 ⬅️", callback_data ="cbstart")
                 ] 
             ]
         )
         )



@Client.on_callback_query(filters.regex("sudo"))
async def sudo(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBotun Sahip komutları 👨‍💻\n\n » /broadcast =>  yayın yapmak ! \n » /broadcast_pin => yayını gruplarda sabitleme ! \n » /gban => küresel yasaklama ! \n » /ungban => küresel yasağı kaldırma ! \n » /alive => botun çalışma durumunu gösterir ! \n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⬅️ 𝖦𝖾𝗋𝗂 ⬅️", callback_data ="admin")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""● **𝖬𝖾𝗋𝗁𝖺𝖻𝖺** {query.from_user.mention} \n\n● **𝖡𝖾𝗇** {bot} !\n\n● **𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻𝖾𝗍𝗅𝖾𝗋𝖽𝖾 müzik 𝖢𝖺𝗅𝖺𝖻𝗂𝗅𝖾𝗇 𝖡𝗈𝗍𝗎𝗆 . . !** \n\n● **𝖡𝖺𝗇 𝖸𝖾𝗍𝗄𝗂𝗌𝗂𝗓, 𝖲𝖾𝗌 𝖸𝗈𝗇𝖾𝗍𝗂𝗆 𝖸𝖾𝗍𝗄𝗂𝗌𝗂 𝗏𝖾𝗋𝗂𝗉 𝖠𝗌𝗂𝗌𝗍𝖺𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾𝗒𝗂𝗇 . . !**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎉 𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾 🎉", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋", callback_data= "admin"
                    ),
                    InlineKeyboardButton(
                        "🇹🇷 𝖢𝗁𝖺𝗇𝗇𝖾𝗅", url=f"https://t.me/StarBotKanal"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧑🏻‍💻 ɢɪᴛʜᴜʙ ᴋᴀʏɴᴀᴋ ᴋᴏᴅᴜ 🧑🏻‍💻", url="https://github.com/MehmetAtes21/music"
                    )
                ]

           ]
        ),
    )

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**• Merhaba şuan aktif olarak çalışmaktayım yardım için aşağıda buttonu kullanınız !**""",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 𝖸𝖺𝗋𝖽𝗂𝗆", url=f"https://t.me/{BOT_USERNAME}?start")]])
    )



@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(c: Client, message: Message):
    chat_id = message.chat.id
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📣 ᴅᴇsᴛᴇᴋ", url=f"https://t.me/{SUPPORT_GROUP}"),
                InlineKeyboardButton(
                    "🗯️ ʙɪʟɢɪ", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**• ᴍᴇʀʜᴀʙᴀ {message.from_user.mention()} {BOT_NAME}**\n\n🧑🏼‍💻 sᴀʜɪʙɪᴍ: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n👾 ʙᴏᴛ ᴠᴇʀsɪᴏɴ: `v{__version__}`\n🔥 ᴘʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ: `{pyrover}`\n🐍 ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: `{__python_version__}`\n✨ PʏTɢCᴀʟʟs ᴠᴇʀsɪᴏɴ: `{pytover.__version__}`\n🆙 ᴄᴀʟɪsᴍᴀ ᴅᴜʀᴜᴍᴜ: `{uptime}`\n\n❤ **Bᴇɴɪ ɢʀᴜʙᴀ ᴀʟᴅɪɢɪɴɪᴢ ɪᴄɪɴ ᴛᴇsᴇᴋᴋᴜʀʟᴇʀ . . !**"

    await c.send_photo(
        chat_id,
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )




@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


chat_watcher_group = 5

@Client.on_message(group=chat_watcher_group)
async def chat_watcher_func(_, message: Message):
    try:
        userid = message.from_user.id
    except Exception:
        return
    suspect = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    if await is_gbanned_user(userid):
        try:
            await message.chat.ban_member(userid)
        except Exception:
            return
        await message.reply_text(
            f"👮🏼 (> {suspect} <)\n\n**Yasaklı** kullanıcı algılandı, bu kullanıcı sudo kullanıcısı tarafından yasaklandı ve bu Sohbetten engellendi !\n\n🚫 **Sebep:** potansiyel spam ve suistimalci."
        )
