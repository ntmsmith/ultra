
from pyultra import *
from pyultra.dB.database import Var
from pyultra.functions.all import *
from telethon import Button, custom

from strings import get_languages, get_string

OWNER_NAME = ultra_bot.me.first_name
OWNER_ID = ultra_bot.me.id


async def setit(event, name, value):
    try:
        udB.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")
