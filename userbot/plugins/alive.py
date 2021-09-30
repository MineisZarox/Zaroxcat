#This is plugin in modified by @MinsisZarox
import random
import re
import time
from platform import python_version
from datetime import datetime

from telethon import version
from telethon.events import CallbackQuery

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import StartTime, catub, catversion, mention

ANIME_QUOTE = [
    "✮ One’s act, one’s profit 🖤",
    "✮ Ten men, ten colors 🖤",
    "✮ Wake from death and return to life 🖤",
    "✮ Evil cause, evil effect 🖤",
    "✮ The weak are meat; the strong eat 🖤",
    "✮ Drunken life, dreamy death 🖤",
    "✮ One life, one encounter  🖤",
    "✮ Different body, same mind 🖤",
    "✮ Meeting person always separated 🖤",
    "✮ Beautiful person, thin life 🖤",
    "✮ Work of self, obtainment of self 🖤",
    "✮ If you do not enter the tiger’s cave, you will not catch its cub  🖤",
    "✮ Even monkeys fall from trees 🖤",
    "✮ There are even bugs that eat knotweed 🖤",
    "✮ Spilt water will not return to the tray 🖤",
    "✮ Gold coins to a cat 🖤",
    "✮ A frog in a well does not know the great sea 🖤",
    "✮ One who chases after two hares won’t catch even one 🖤",
    "✮ An apprentice near a temple will recite the scriptures untaught  🖤",
    "✮ Fall down seven times, stand up eight 🖤",
    "✮ Unless an idiot dies, he won’t be cured 🖤",
    "✮ Give up on your dreams and die 🖤",
]
plugin_category = "utils"
botusername = Config.TG_BOT_USERNAME

@catub.cat_cmd(
    pattern="alive$",
    command=("alive", plugin_category),
    info={
        "header": "To check bot's alive status,",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    start = datetime.now()
    ANIME = f"{random.choice(ANIME_QUOTE)}"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✧✧"
    CUSTOM_ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or ANIME
    CAT_IMG = gvarstatus("ALIVE_PIC")
    end = datetime.now()
    if CAT_IMG:
        CAT = [x for x in CAT_IMG.split()]
        A_IMG = list(CAT)
        PIC = random.choice(A_IMG)
        ms = (end - start).microseconds / 1000
        cat_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        cat_caption += f"┏━━━━━━━━━━━━━━━━┓\n"
        cat_caption += f"┃**{EMOJI} ᴜꜱᴇʀʙᴏᴛ ᴠᴇʀꜱɪᴏɴ:** `{catversion}`\n"
        cat_caption += f"┃**{EMOJI} ᴅᴇᴀᴅ ꜱɪɴᴄᴇ:** `{uptime}\n`"
        cat_caption += f"┃**{EMOJI} ꜱᴇɴꜱᴇɪ:** {mention}\n"
        cat_caption += f"┃**{EMOJI} ꜱᴛᴀᴛᴜꜱ:** `{check_sgnirts}`\n"
        cat_caption += f"┗━━━━━━━━━━━━━━━━┛\n"
        cat_caption += f"┏━━━━━━━━━━━━━━┓\n┃ ⁭⁫**{EMOJI} ᴘɪɴɢ :** {ms} ms \n┗━━━━━━━━━━━━━━┛\n"
        await event.client.send_file(
            event.chat_id,
            PIC,
            caption=cat_caption,
            reply_to=reply_to_id,
            allow_cache=True,
        )
        await event.delete()
    else:
        await edit_or_reply(
            event,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"**{EMOJI} Database :** `{check_sgnirts}`\n"
            f"**{EMOJI} Telethon Version :** `{version.__version__}\n`"
            f"**{EMOJI} Catuserbot Version :** `{catversion}`\n"
            f"**{EMOJI} Python Version :** `{python_version()}\n`"
            f"**{EMOJI} Uptime :** `{uptime}\n`"
            f"**{EMOJI} Master:** {mention}\n",
        )

@catub.bot_cmd(
    pattern=f"^/alive?([\s]+)?$"
)
async def amireallyalive(event):
    start = datetime.now()
    ANIME = f"{random.choice(ANIME_QUOTE)}"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✧✧"
    CUSTOM_ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or ANIME
    CAT_IMG = gvarstatus("ALIVE_PIC")
    await event.delete()
    end = datetime.now()
    if CAT_IMG:
        CAT = [x for x in CAT_IMG.split()]
        A_IMG = list(CAT)
        PIC = random.choice(A_IMG)
        ms = (end - start).microseconds / 1000
        cat_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"
        cat_caption += f"┏━━━━━━━━━━━━━━━━┓\n"
        cat_caption += f"┃**{EMOJI} ᴜꜱᴇʀʙᴏᴛ ᴠᴇʀꜱɪᴏɴ:** `{catversion}`\n"
        cat_caption += f"┃**{EMOJI} ᴅᴇᴀᴅ ꜱɪɴᴄᴇ:** `{uptime}\n`"
        cat_caption += f"┃**{EMOJI} ꜱᴇɴꜱᴇɪ:** {mention}\n"
        cat_caption += f"┃**{EMOJI} ꜱᴛᴀᴛᴜꜱ:** `{check_sgnirts}`\n"
        cat_caption += f"┗━━━━━━━━━━━━━━━━┛\n"
        cat_caption += f"┏━━━━━━━━━━━━━━┓\n┃ ⁭⁫**{EMOJI} ᴘɪɴɢ :** {ms} ms \n┗━━━━━━━━━━━━━━┛\n"
        await event.client.send_file(
            event.chat_id,
            PIC,
            caption=cat_caption,
            reply_to=reply_to_id,
            allow_cache=True,
        )
    else:
        await event.respond(
            f"**{ANIME}**\n\n"
            f"**{EMOJI} Database :** `{check_sgnirts}`\n"
            f"**{EMOJI} Telethon Version :** `{version.__version__}\n`"
            f"**{EMOJI} Catuserbot Version :** `{catversion}`\n"
            f"**{EMOJI} Python Version :** `{python_version()}\n`"
            f"**{EMOJI} Uptime :** `{uptime}\n`"
            f"**{EMOJI} Master:** {mention}\n",
        )
