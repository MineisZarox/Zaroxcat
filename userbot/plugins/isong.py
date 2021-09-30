#By @Feelded
from userbot import catub
from ..core.managers import edit_delete
from ..helpers.utils import reply_id
from ..helpers.functions import deEmojify, hide_inlinebot
plugin_category = "useless"

@catub.cat_cmd(
    pattern="isong ?(.*)",
    command=("isong", plugin_category),
    info={
        "header": "Inline music downloader by @FeelDeD",
        "usage": [
            "{tr}isong <song name>",
        ],
    },
)
async def music(event):
    "Download song through @Deezermusicbot"
    if event.fwd_from:
        return
    bot = "@deezermusicbot"
    music = event.pattern_match.group(1)
    music = deEmojify(music)
    reply_to_id = await reply_id(event)
    if not music:
        return await edit_delete(
            event, "What should i search? Give a song name"
        )
    await event.delete()
    await hide_inlinebot(event.client, bot, music, event.chat_id, reply_to_id)