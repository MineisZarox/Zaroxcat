#By @IrisZarox
import os
import heroku3
import shutil as sl
from ..Config import Config
from ..utils import load_plugins, remove_plugin as rem
from . import catub, edit_delete, edit_or_reply, UPSTREAM_REPO_URL

plugin_category = "tools"

z, y, x, w, v, = UPSTREAM_REPO_URL.split("/")
branch = Config.UPSTREAM_REPO_BRANCH or "master"
# =================================================
Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY
# =================================================


# =================================================
repo = os.environ.get("EXTERNAL_PLUGIN_REPO")
token = os.environ.get("GITHUB_ACCESS_TOKEN")
a, b, c, username, d, = repo.split("/")
ppr = c + "/" + username + "/"  + d
if token:
    plug_repo = f"https://{username}:{token}@{ppr}.git"
else:
    plug_repo = repo
# =================================================
    
@catub.cat_cmd(
    pattern="(refresh|re)( -def)$",
    command=("refresh", plugin_category),
    info={
        "header": "To refresh all external plugin.",
        "description": "Reinstall all external plugins from external plugin repository.",
        "usage": "{tr}refresh",
    },
)

async def refesh(event):
    def = event.pattern_match.group(2)
    if def:
        exact_fld = "plugins"
        repo = f"--single-branch --branch {branch} {UPSTREAM_REPO_URL}"
        fld = f"{v}/userbot/plugins"
        repo_fld = v
    else:
        exact_fld = "ext_plugins"
        repo = plug_repo
        fld = f"{d}/ext/plugins"
        repo_fld = d
    try:
        k = os.listdir(f"userbot/{exact_fld}")
        res = [sub.replace('.py', '') for sub in k]
        for i in res:
            rem(i)
        sl.rmtree(f"userbot/{exact_fld}}")
        os.system(f"git clone {repo}")
        os.system(f"mv '{fld}' 'userbot'")
        sl.rmtree(repo_fld)
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        await load_plugins("ext_plugins")
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            app = Heroku.app(HEROKU_APP_NAME)
            data = app.get_log()
            await edit_or_reply(event, data, deflink=True, linktext="`Refreshed all external plugins successfully: `")
        except BaseException:
            return await edit_or_reply(event, "`Refreshed all external plugins successfully`")
    except Exception as e:
        LOGS.error(f"{e}")
