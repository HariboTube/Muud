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
                caption=(f"""β **π¬πΎπππΊπ»πΊ** {message.from_user.mention} \n\nβ **π‘πΎπ** {BOT_NAME}!\n\nβ **π²πΎπππ π²πππ»πΎπππΎππ½πΎ mΓΌzik π’πΊππΊπ»πππΎπ π‘ππππ . . !** \n\nβ **π‘πΊπ πΈπΎππππππ, π²πΎπ πΈπππΎπππ πΈπΎπππππ ππΎπππ π πππππΊππ π¦πππ»πΊ π€πππΎπππ . . !**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π π‘πΎππ π¦πππ»πΊ π€πππΎ π", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π πͺππππππΊπ", callback_data= "admin"
                    ),
                    InlineKeyboardButton(
                        "πΉπ· π’ππΊπππΎπ", url="https://t.me/StarBotKanal"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π§π»βπ» Ι’Ιͺα΄Κα΄Κ α΄α΄ΚΙ΄α΄α΄ α΄α΄α΄α΄ π§π»βπ»", url="https://github.com/MehmetAtes21/music"
                    )
                ]
                
           ]
        ),
    )

@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>πΉπ· TΓΌm Komutlar : \n\nΒ» /vbul => α΄ Ιͺα΄α΄α΄ ΙͺΙ΄α΄ΙͺΚ . \nΒ» /bul => α΄α΄α΄’Ιͺα΄ ΙͺΙ΄α΄ΙͺΚ . \nΒ» /oynat => α΄α΄α΄’Ιͺα΄ α΄ΚΙ΄α΄α΄ . \nΒ» /durdur => α΄α΄α΄’ΙͺΙ’Ιͺ α΄α΄Κα΄α΄Κ . \nΒ» /devam => α΄α΄α΄’ΙͺΙ’Ιͺ sα΄Κα΄α΄Κ . \nΒ» /atla =>  α΄α΄α΄’ΙͺΙ’Ιͺ α΄α΄Κα΄ . \nΒ» /son => α΄α΄α΄’ΙͺΙ’Ιͺ sα΄Ι΄Κα΄Ι΄α΄ΙͺΚ . \nΒ» /katil => α΄sΙͺsα΄α΄Ι΄Ιͺ Ι’Κα΄Κα΄ α΄α΄α΄ α΄α΄ α΄α΄α΄Κ . \nΒ» /reload => α΄α΄α΄ΙͺΙ΄ ΚΙͺsα΄α΄sΙͺΙ΄Ιͺ Ι’α΄Ι΄α΄α΄ΚΚα΄Κ . \n\nΒ» /auth => α΄α΄ΚΚα΄Ι΄Ιͺα΄ΙͺΙ΄ΙͺΙ΄ Κα΄Ι΄α΄α΄Ιͺα΄Ιͺ α΄Κα΄α΄α΄ΙͺΙ’Ιͺ Κα΄Κα΄α΄ α΄α΄α΄α΄α΄Κα΄ΚΙͺ α΄α΄ΚΚα΄Ι΄α΄α΄sΙͺΙ΄α΄ Ιͺα΄’ΙͺΙ΄ α΄ α΄ΚΙͺΚ . \n\nΒ» /unauth => α΄α΄ΚΚα΄Ι΄Ιͺα΄ΙͺΙ΄ΙͺΙ΄ Κα΄Ι΄α΄α΄Ιͺα΄Ιͺ α΄Κα΄α΄α΄ΙͺΙ’Ιͺ Κα΄Κα΄α΄ α΄α΄α΄α΄α΄Κα΄ΚΙͺ α΄α΄ΚΚα΄Ι΄α΄α΄sΙͺΙ΄Ιͺ α΄Ι΄Ι’α΄ΚΚα΄Κ . </b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "πΉπ· π πππππΊπ", url="https://t.me/StarMuzikAsistan"
                     ),
                     InlineKeyboardButton(
                         "π§π»βπ» π?πππΎπ", url="https://t.me/Hayiboo"
                     )
                 ],
                 [
                     InlineKeyboardButton(
                         "βπ» π²πΊπππ πͺππππππΊππ", callback_data ="sudo"
                     )
                 ],
                 [
                     InlineKeyboardButton(
                         "β¬οΈ π¦πΎππ β¬οΈ", callback_data ="cbstart")
                 ] 
             ]
         )
         )



@Client.on_callback_query(filters.regex("sudo"))
async def sudo(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Selam {query.from_user.mention}!\nBotun Sahip komutlarΔ± π¨βπ»\n\n Β» /broadcast =>  yayΔ±n yapmak ! \n Β» /broadcast_pin => yayΔ±nΔ± gruplarda sabitleme ! \n Β» /gban => kΓΌresel yasaklama ! \n Β» /ungban => kΓΌresel yasaΔΔ± kaldΔ±rma ! \n Β» /alive => botun Γ§alΔ±Εma durumunu gΓΆsterir ! \n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "β¬οΈ π¦πΎππ β¬οΈ", callback_data ="admin")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""β **π¬πΎπππΊπ»πΊ** {query.from_user.mention} \n\nβ **π‘πΎπ** {BOT_NAME} !\n\nβ **π²πΎπππ π²πππ»πΎπππΎππ½πΎ mΓΌzik π’πΊππΊπ»πππΎπ π‘ππππ . . !** \n\nβ **π‘πΊπ πΈπΎππππππ, π²πΎπ πΈπππΎπππ πΈπΎπππππ ππΎπππ π πππππΊππ π¦πππ»πΊ π€πππΎπππ . . !**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π π‘πΎππ π¦πππ»πΊ π€πππΎ π", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π πͺππππππΊπ", callback_data= "admin"
                    ),
                    InlineKeyboardButton(
                        "πΉπ· π’ππΊπππΎπ", url=f"https://t.me/StarBotKanal"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π§π»βπ» Ι’Ιͺα΄Κα΄Κ α΄α΄ΚΙ΄α΄α΄ α΄α΄α΄α΄ π§π»βπ»", url="https://github.com/MehmetAtes21/music"
                    )
                ]

           ]
        ),
    )

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**β’ Merhaba Εuan aktif olarak Γ§alΔ±ΕmaktayΔ±m yardΔ±m iΓ§in aΕaΔΔ±da buttonu kullanΔ±nΔ±z !**""",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("π πΈπΊππ½ππ", url=f"https://t.me/{BOT_USERNAME}?start")]])
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
                InlineKeyboardButton("π£ α΄α΄sα΄α΄α΄", url=f"https://t.me/{SUPPORT_GROUP}"),
                InlineKeyboardButton(
                    "π―οΈ ΚΙͺΚΙ’Ιͺ", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**β’ α΄α΄ΚΚα΄Κα΄ {message.from_user.mention()} {BOT_NAME}**\n\nπ§πΌβπ» sα΄ΚΙͺΚΙͺα΄: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\nπΎ Κα΄α΄ α΄ α΄ΚsΙͺα΄Ι΄: `v{__version__}`\nπ₯ α΄Κα΄Ι’Κα΄α΄ α΄ α΄ΚsΙͺα΄Ι΄: `{pyrover}`\nπ α΄Κα΄Κα΄Ι΄ α΄ α΄ΚsΙͺα΄Ι΄: `{__python_version__}`\nβ¨ PΚTΙ’Cα΄ΚΚs α΄ α΄ΚsΙͺα΄Ι΄: `{pytover.__version__}`\nπ α΄α΄ΚΙͺsα΄α΄ α΄α΄Κα΄α΄α΄: `{uptime}`\n\nβ€ **Bα΄Ι΄Ιͺ Ι’Κα΄Κα΄ α΄Κα΄ΙͺΙ’ΙͺΙ΄Ιͺα΄’ Ιͺα΄ΙͺΙ΄ α΄α΄sα΄α΄α΄α΄ΚΚα΄Κ . . !**"

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
    await m_reply.edit_text("π `PONG!!`\n" f"β‘οΈ `{delta_ping * 1000:.3f} ms`")


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
            f"π?πΌ (> {suspect} <)\n\n**YasaklΔ±** kullanΔ±cΔ± algΔ±landΔ±, bu kullanΔ±cΔ± sudo kullanΔ±cΔ±sΔ± tarafΔ±ndan yasaklandΔ± ve bu Sohbetten engellendi !\n\nπ« **Sebep:** potansiyel spam ve suistimalci."
        )
