import os
from ..utils import remove_plugin as rem
from . import catub, edit_delete, edit_or_reply

repo = os.environ.get("EXTERNAL_PLUGIN_REPO")
token = os.environ.get("GITHUB_ACCESS_TOKEN")
a, b, c, username, d, = repo.split("/")
ppr = c + "/" + username + "/"  + d
if token:
    plug_repo = f"https://{username}:{token}@{ppr}.git"
else:
    plug_repo = repo

@catub.cat_cmd(
    pattern="(refresh|re)$",
    command=("refresh", plugin_category),
    info={
        "header": "To refresh all external plugin.",
        "description": "Reinstall all external plugins from external plugin repository.",
        "usage": "{tr}refresh",
    },
)

async def refesh(event):
    try:
        k = os.listdir("userbot/ext_plugins")
        res = [sub.replace('.py', '') for sub in k]
        for i in res:
            rem(i)
        os.system("rm -rf ext_plugins")
        os.system(f"git clone {plug_repo}")
        os.system("mv 'Plugins/ext_plugins' 'userbot'")
        os.system("rm -rf Plugins")
        await edit_or_reply(event, "`Refreshed all ext plugins successfully`")
    except Exception as e:
        LOGS.error(f"{e}")
