"""
✘ Commands Available -

• `{i}rename <file name with extension>`
    rename the file
    
• `{i}mtoi <reply to media>`
    media to image conversion

• `{i}mtos <reply to media>`
    convert media to sticker.
"""

import os

import cv2
from PIL import Image

from . import *


@Ultra_cmd(pattern="rename ?(.*)")
async def imak(event):
    reply = await event.get_reply_message()
    if not reply:
        await eor(event, "Reply to any media/Document.")
        return
    inp = event.pattern_match.group(1)
    if not inp:
        await eor(event, "Give The name nd extension of file")
        return
    xx = await eor(event, "`Processing...`")
    image = await Ultra_bot.download_media(reply)
    os.rename(image, inp)
    await Ultra_bot.send_file(event.chat_id, inp, force_document=True, reply_to=reply)
    os.remove(inp)
    await xx.delete()


@Ultra_cmd(pattern="mtoi$")
async def imak(event):
    reply = await event.get_reply_message()
    if not (reply and (reply.media)):
        await eor(event, "Reply to any media.")
        return
    xx = await eor(event, "`Processing...`")
    image = await Ultra_bot.download_media(reply)
    file = "ult.png"
    if image.endswith((".webp", ".png")):
        c = Image.open(image)
        c.save(file)
    else:
        img = cv2.VideoCapture(image)
        ult, roid = img.read()
        cv2.imwrite(file, roid)
    await Ultra_bot.send_file(event.chat_id, file, reply_to=reply)
    await xx.delete()
    os.remove(file)
    os.remove(image)


@Ultra_cmd(pattern="mtos$")
async def smak(event):
    reply = await event.get_reply_message()
    if not (reply and (reply.media)):
        await eor(event, "Reply to any media.")
        return
    xx = await eor(event, "`Processing...`")
    image = await Ultra_bot.download_media(reply)
    file = "ult.webp"
    if image.endswith((".webp", ".png", ".jpg")):
        c = Image.open(image)
        c.save(file)
    else:
        img = cv2.VideoCapture(image)
        ult, roid = img.read()
        cv2.imwrite(file, roid)
    await Ultra_bot.send_file(event.chat_id, file, reply_to=reply)
    await xx.delete()
    os.remove(file)
    os.remove(image)


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
