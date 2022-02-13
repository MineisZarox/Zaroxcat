#By https://t.me/irisZarox
import os
import subprocess

from ..Config import Config
from ..utils import load_module, remove_plugin
from . import CMD_HELP, CMD_LIST, SUDO_LIST, catub, edit_delete, edit_or_reply, hmention, reply_id

repo = os.environ.get("EXTERNAL_PLUGIN_REPO")
token = os.environ.get("GITHUB_ACCESS_TOKEN")
a, b, c, username, d, = repo.split("/")
ppr = c + "/" + username + "/"  + d
if token:
    plug_repo = f"https://{username}:{token}@{ppr}.git"
else:
    plug_repo = repo

async def unload_plugins(folder):
    """
    To unload plugins from the mentioned folder
    """
    path = f"userbot/{folder}/*.py"
    files = glob.glob(path)
    files.sort()
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                if shortname.replace(".py", "") not in Config.NO_LOAD:
                    flag = True
                    check = 0
                    while flag:
                        try:
                            remove_plugin(
                                shortname.replace(".py", ""),
                                plugin_path=f"userbot/{folder}",
                            )
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"userbot/{folder}/{shortname}.py"))
            except Exception as e:
                os.remove(Path(f"userbot/{folder}/{shortname}.py"))
                LOGS.info(f"unable to load {shortname} because of error {e}")

@catub.cat_cmd(
    pattern="refresh $",
    command=("refresh", plugin_category),
    info={
        "header": "To install an external plugin.",
        "description": "Reply to any external plugin(supported by cat) to install it in your bot.",
        "usage": "{tr}refresh",
    },
)
async def refesh(event):
    ""
    await unload_plugins(external_plugins)
    os.system("rm -rf external_plugins")
    catevent = await edit_or_reply("`Removing old Plugins`")
    try:
        clone = os.system(f"git clone {plug_repo}")
        if clone != 0:
            os.system(f"git clone {repo}")
        os.system("mv 'Plugins/external_plugins' 'userbot'")
        os.system("rm -rf Plugins")
        await catevent.edit("`Refreshed all external plugins`")
    except Exception as e:
        LOGS.error(f"{e}")
