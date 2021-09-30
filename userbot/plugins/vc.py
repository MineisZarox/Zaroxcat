#By @FeelDeD
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.phone import CreateGroupCallRequest
from telethon.tl.functions.phone import DiscardGroupCallRequest
from telethon.tl.functions.phone import GetGroupCallRequest
from telethon.tl.functions.phone import InviteToGroupCallRequest
from userbot import catub

plugin_category = "useless"

async def getvc(event):
    chat_ = await event.client(GetFullChannelRequest(event.chat_id))
    _chat = await event.client(GetGroupCallRequest(chat_.full_chat.call))
    return _chat.call

def all_users(a, b):
    for c in range(0, len(a), b):
        yield a[c : c + b]


@catub.cat_cmd(
    pattern="startvc$",
    command=("startvc", plugin_category),
    info={
        "header": "Join Voice Chat",
        "usage": [
            "{tr}startvc",
        ],
    },
)
async def _(event):
    "Start voicechat"
    try:
        await event.client(CreateGroupCallRequest(event.chat_id))
        await event.edit("`Voice Chat Started Successfully`")
    except Exception as e:
        await event.edit( f"`{str(e)}`")

@catub.cat_cmd(
    pattern="endvc$",
    command=("endvc", plugin_category),
    info={
        "header": "End Voice Chat",
        "usage": [
            "{tr}endvc",
        ],
    },
)
async def _(event):
    "End voicechat"
    try:
        await bot(DiscardGroupCallRequest(await getvc(event)))
        await event.edit("`Voice Chat Ended Successfully`")
    except Exception as e:
        await event.edit( f"`{str(e)}`")
