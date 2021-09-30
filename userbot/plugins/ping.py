import asyncio
from datetime import datetime

from userbot import catub

from ..core.managers import edit_or_reply

plugin_category = "tools"


@catub.cat_cmd(
    pattern="ping( -a|$)",
    command=("ping", plugin_category),
    info={
        "header": "check how long it takes to ping your userbot",
        "flags": {"-a": "average ping"},
        "usage": ["{tr}ping", "{tr}ping -a"],
    },
)
async def _(event):
    "To check ping"
    flag = event.pattern_match.group(1)
    if flag == " -a":
        start = datetime.now()
        catevent = await edit_or_reply(event, "`!....`")
        await asyncio.sleep(0.3)
        await catevent.edit("`..!..`")
        await asyncio.sleep(0.3)
        await catevent.edit("`....!`")
        end = datetime.now()
        tms = (end - start).microseconds / 1000
        ms = round((tms - 0.6) / 3, 3)
        await catevent.edit(f"Average Pong!\n`{ms} ms`")
    else:
        start = datetime.now()
        catevent = await edit_or_reply(event, "Pong!")
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await catevent.edit(f"Pong!\n`{ms} ms`")
        
        


@catub.bot_cmd(
    pattern=f"^/ping?([\s]+)?$",
)
async def _(event):
    start = datetime.now()
    catevent = await event.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await catevent.edit(f"Pong!\n`{ms} ms`")
