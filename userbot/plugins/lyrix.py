#By @feelded
import requests
from userbot import catub
from ..core.managers import edit_or_reply, edit_delete

plugin_category = "useless"

@catub.cat_cmd(
    pattern="lyrix ?(.*)",
    command=("lyrix", plugin_category),
    info={
        "header": "Song lyrics searcher",
        "description": "if you want to provide artist name with song name, Will be better (Loser - Neoni)",
        "usage": [
            "{tr}lyrix <song name>",
        ],
        "examples": [
            "{tr}lyrix death bed",
        ],
    },
)
async def lyrics(odi):
    "To get song lyrics"
    songname = odi.pattern_match.group(1)
    if not songname:
    	await edit_delete(odi, "`Give me a song name`", 6)
    else:
    	await edit_or_reply(odi, f"`Searching lyrics for {songname} ...`")
    	x = requests.get(f'https://botzhub.herokuapp.com/lyrics?song={songname}').json()
    	artist = lyrics = ""
    	try:
    		artist = x['artist']
    		lyrics = x['lyrics']
    	except:
    		lyrics = x['lyrics']
    	
    		if artist == "":
    			await edit_or_reply(odi, f"**Song:** `{songname}`\n\n`{lyrics}`")
    		else:
    			await edit_or_reply(odi, f"**Song:** `{songname}`\n**Artist:** {artist}\n\n`{lyrics}`")
