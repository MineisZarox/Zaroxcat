#By @MineisZarox, idea by @Feelded
import random
from userbot import catub 
from ..helpers.utils import edit_or_reply, edit_delete
from datetime import datetime
from . import get_user_from_event
import asyncio

plugin_category = "extra"

@catub.cat_cmd(
    pattern="xban(?:\s|$)([\s\S]*)",
    command=("xban", plugin_category),
    info={
        "header": "To ban user in every group where you are admin(fake).",
        "description": "Will ban the person in every group where you are admin only.",
        "usage": "{tr}xban <username/reply/userid> <reason (optional)>",
    },
)
async def catgban(event):  # sourcery no-metrics
    "To ban user in every group where you are admin."
    cate = await edit_or_reply(event, "`gbanning.......`")
    user, reason = await get_user_from_event(event, cate)
    if not user:
        return
    if user.id == catub.uid:
        return await edit_delete(cate, "`why would I ban myself`")
    else:
        pass
    await asyncio.sleep(1)
    san = random.choice(range(90, 135))
    await cate.edit(
        f"`initiating gban of the `[user](tg://user?id={user.id}) `in {san} groups`"
    )
    await asyncio.sleep(2)
    cattaken = random.choice(range(8, 17))
    await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was gbanned in {san} groups in {cattaken} seconds`!!"
        )
        
@catub.cat_cmd(
    pattern="unxban(?:\s|$)([\s\S]*)",
    command=("unxban", plugin_category),
    info={
        "header": "To unban user in every group where you are admin(fake).",
        "description": "Will unban the person in every group where you are admin only.",
        "usage": "{tr}unxban <username/reply/userid> <reason (optional)>",
    },
)
async def catgban(event):  # sourcery no-metrics
    "To unban user in every group where you are admin."
    cate = await edit_or_reply(event, "`ungbanning.......`")
    user, reason = await get_user_from_event(event, cate)
    if not user:
        return
    if user.id == catub.uid:
        return await edit_delete(cate, "`why would I ungban myself`")
    else:
        pass
    await asyncio.sleep(1)
    san = random.choice(range(90, 135))
    await cate.edit(
        f"`initiating ungban of the `[user](tg://user?id={user.id}) `in {san} groups`"
    )
    await asyncio.sleep(2)
    cattaken = random.choice(range(8, 17))
    await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was ungbanned in {san} groups in {cattaken} seconds`!!"
        )
        
@catub.cat_cmd(
    pattern="xmute(?:\s|$)([\s\S]*)",
    command=("xmute", plugin_category),
    info={
        "header": "To mute user in every group where you are admin(fake).",
        "description": "Will mute the person in every group where you are admin only.",
        "usage": "{tr}xmute <username/reply/userid> <reason (optional)>",
    },
)
async def catgban(event):  # sourcery no-metrics
    "To mute user in every group where you are admin."
    cate = await edit_or_reply(event, "`processing.......`")
    user, reason = await get_user_from_event(event, cate)
    if not user:
        return
    if user.id == catub.uid:
        return await edit_delete(cate, "`why would I ban myself`")
    else:
        pass
    san = random.choice(range(90, 135))
    await asyncio.sleep(3)
    cattaken = random.choice(range(8, 17))
    await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `is Successfully gmuted in {san} groups in {cattaken} seconds`!!"
        )

@catub.cat_cmd(
    pattern="unxmute(?:\s|$)([\s\S]*)",
    command=("unxmute", plugin_category),
    info={
        "header": "To remove gmute on that person.(fake).",
        "description": "Will unmute the person in every group where you are admin only.",
        "usage": "{tr}unxmute <username/reply/userid> <reason (optional)>",
    },
)
async def catgban(event):  # sourcery no-metrics
    "To remove gmute on that person."
    cate = await edit_or_reply(event, "`processing.......`")
    user, reason = await get_user_from_event(event, cate)
    if not user:
        return
    if user.id == catub.uid:
        return await edit_delete(cate, "`why would I ban myself`")
    else:
        pass
    san = random.choice(range(90, 135))
    await asyncio.sleep(3)
    cattaken = random.choice(range(8, 17))
    await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `is Successfully unmuted in {san} groups in {cattaken} seconds`!!"
        )

@catub.cat_cmd(
    pattern="xkick(?:\s|$)([\s\S]*)",
    command=("xkick", plugin_category),
    info={
        "header": "kicks the person in all groups where you are admin.(fake).",
        "description": "Will kick the person in every group where you are admin only.",
        "usage": "{tr}xban <username/reply/userid> <reason (optional)>",
    },
)
async def catgban(event):  # sourcery no-metrics
    "kicks the person in all groups where you are admin."
    cate = await edit_or_reply(event, "`gkicking.......`")
    user, reason = await get_user_from_event(event, cate)
    if not user:
        return
    if user.id == catub.uid:
        return await edit_delete(cate, "`why would I ban myself`")
    else:
        pass
    await asyncio.sleep(1)
    san = random.choice(range(90, 135))
    await cate.edit(
        f"`initiating gban of the `[user](tg://user?id={user.id}) `in {san} groups`"
    )
    await asyncio.sleep(2)
    cattaken = random.choice(range(8, 17))
    await cate.edit(
            f"[{user.first_name}](tg://user?id={user.id}) `was gkicked in {san} groups in {cattaken} seconds`!!"
        )