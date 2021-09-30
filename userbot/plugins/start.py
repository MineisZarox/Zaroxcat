from userbot import catub
import os
from ..Config import Config
from ..helpers.utils import reply_id

PIC = os.environ.get("PIC", "https://telegra.ph/file/360adbb434e877f5bf790.mp4")
botusername = Config.TG_BOT_USERNAME

@catub.bot_cmd(
    pattern=f"^/start({botusername})?([\s]+)?$",
)
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    await event.client.send_file(event.chat_id, PIC, caption=f"!Hola\nI am zaroxcat an experimental bot in which some commands of catuserbot can used universally by anyone\n",  reply_to=reply_to_id, allow_cache=True,)
