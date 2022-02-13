import os
import sys
import subprocess

import userbot
from userbot import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import catub
from .utils import (
    add_bot_to_logger_group,
    ipchange,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("CatUserbot")

print(userbot.__copyright__)
print("Licensed under the terms of the " + userbot.__license__)

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("Starting Userbot")
    catub.loop.run_until_complete(setup_bot())
    LOGS.info("TG Bot Startup Completed")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()
    


plug_repo = os.environ.get("EXTERNAL_PLUGIN_REPO") or "https://github.com/MineisZarox/Plugins"
a, b, c, username, d, = plug_repo.split("/")
token = os.environ.get("GITHUB_ACCESS_TOKEN")
ppr = str(plug_repo)[-8:]
plug_private_repo = f"https://{username}:{token}@{ppr}.git"

try:
    kk = os.system(f"git clone {plug_repo}")
    if kk == 0:
        pass
    else:
        k = os.system(f"git clone {}")
        sed = subprocess.run([f"git clone {plug_private_repo}"], shell=True, capture_output=True)
        if 'fatal' in str(sed.stderr):
            print(str(sed.stderr)[-1:])
            print("")
    os.system("mv 'Plugins/external_plugins' 'userbot'")
    os.system("rm -rf Plugins")
except Exception as e:
    LOGS.error(f"{e}")

class CatCheck:
    def __init__(self):
        self.sucess = True


Catcheck = CatCheck()


async def startup_process():
    check = await ipchange()
    if check is not None:
        Catcheck.sucess = False
        return
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print("Importing External plugins")
    await load_plugins("external_plugins")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("Yay your userbot is officially working.!!!")
    print(
        f"Congratulation, now type {cmdhr}alive to see message if catub is live\
        \nIf you need assistance, head to https://t.me/catuserbot_support"
    )
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Catcheck.sucess = True
    return


catub.loop.run_until_complete(startup_process())


if len(sys.argv) not in (1, 3, 4):
    catub.disconnect()
elif not Catcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        catub.run_until_disconnected()
    except ConnectionError:
        pass
