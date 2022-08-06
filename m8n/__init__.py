What is an init.py file?
Python defines two types of packages, regular packages and namespace packages. Regular packages are traditional packages as they existed in Python 3.2 and earlier. A regular package is typically implemented as a directory containing an __init__.py file. When a regular package is imported, this __init__.py file is implicitly executed, and the objects it defines are bound to names in the package’s namespace. The __init__.py file can contain the same Python code that any other module can contain, and Python will add some additional attributes to the module when it is imported.

import asyncio
import importlib
from pytgcalls import PyTgCalls
import time
from pyrogram import Client
from m8n import config


SUDO_USERS = config.SUDO_USERS
OWNER_ID = config.OWNER_ID
BOT_ID = config.BOT_ID
BOT_NAME = ""
BOT_USERNAME = ""
ASSID = config.ASSID
ASSNAME = ""
ASSUSERNAME = ""
SUDOERS = SUDO_USERS
OWNER = OWNER_ID

### Boot Time
boottime = time.time()

### auto
smexy = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(smexy)

### Music Start Time
Music_START_TIME = time.time()

app = Client(
    "montaro1",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)


def all_info(app, client):
    global BOT_ID, BOT_NAME, BOT_USERNAME
    global ASSID, ASSNAME, ASSUSERNAME
    getme = app.get_me()
    getme1 = client.get_me()
    BOT_ID = getme.id
    ASSID = getme1.id
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name
    BOT_USERNAME = getme.username
    ASSNAME = (
        f"{getme1.first_name} {getme1.last_name}"
        if getme1.last_name
        else getme1.first_name
    )
    ASSUSERNAME = getme1.username


app.start()
client.start()
all_info(app, client)
