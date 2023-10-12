#By Zarox https://t.me/zarox
import os
import shutil as sl
from ..Config import Config
from ..utils import load_module, load_plugins, remove_plugin as rem
from . import catub, edit_or_reply

plugin_category = "tools"



# =================================================
def get_repo():
    repo = os.environ.get("EXTERNAL_PLUGIN_REPO")
    token = os.environ.get("GITHUB_ACCESS_TOKEN")
    a, b, c, username, d, = repo.split("/")
    ppr = f"{c}/{username}/{d}"
    return f"https://{username}:{token}@{ppr}.git" if token else repo
# =================================================
    
@catub.cat_cmd(
    pattern="refresh(?:\s|$)([\s\S]*)",
    command=("refresh", plugin_category),
    info={
        "header": "To refresh external plugin with repository.",
        "description": "Reinstall external plugins from external plugin repository.",
        "usage": [
            "{tr}refresh",
            "{tr}refresh plugin"
        ],
    },
)
async def refesh(event):
    "To refresh ext_plugins"
    if not os.environ.get("EXTERNAL_PLUGIN_REPO"):
        return await edit_or_reply(event,  "Please set Enviroment variable `EXTERNAL_PLUGIN_REPO`\n\n__Note: This ENV VAR is only used by this perticular plugin.__")
    repo = get_repo()
    if plugin := event.pattern_match.group(1):
        try:
            try:
                rem(plugin)
            except Exception:
                return await edit_or_reply(event, f"`No such plugin exist as {plugin}.py`")
            os.remove(f"userbot/ext_plugins/{plugin}.py")
            os.system(f"git clone {plug_repo}")
            os.system(f"mv 'Plugins/ext_plugins/{plugin}.py' 'userbot/ext_plugins'")
            sl.rmtree("Plugins")
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
            load_module(plugin, "userbot/ext_plugins")
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
            await edit_or_reply(event,  f"`Refreshed {plugin} successfully.`")
        except Exception as e:
            return await edit_or_reply(event,  f"`Error:: {e}`")
    else:
        try:
            k = os.listdir("userbot/ext_plugins")
            res = [sub.replace('.py', '') for sub in k]
            for i in res:
                rem(i)
            await edit_or_reply(event, f"`Cloning to {d}...`")
            sl.rmtree("userbot/ext_plugins")
            os.system(f"git clone {plug_repo}")
            os.system("mv 'Plugins/ext_plugins' 'userbot'")
            sl.rmtree("Plugins")
            await edit_or_reply(event, "`Installing external plugins...`")
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
            await load_plugins("ext_plugins")
            print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
            dir_ = os.listdir("userbot/ext_plugins")
            plug = sum(1 for _ in dir_)
            return await edit_or_reply(event, f"`Refreshed all {plug} external plugins successfully`")
        except Exception as e:
            return await edit_or_reply(event,  f"`Error: {e}`")
