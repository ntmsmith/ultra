"""
✘ Commands Available -

• `{i}webupload`
    Upload files on another server.
"""


import asyncio
import time

from telethon.errors.rpcerrorlist import BotInlineDisabledError as dis
from telethon.errors.rpcerrorlist import BotResponseTimeoutError as rep

from . import *


@Ultra_cmd(
    pattern="webupload",
)
async def _(event):
    xx = await eor(event, "`Processing...`")
    vv = event.text.split(" ", maxsplit=1)
    try:
        file_name = vv[1]
    except IndexError:
        pass
    if event.reply_to_msg_id:
        bb = await event.get_reply_message()
        if bb.media:
            ccc = time.time()
            file_name = await event.client.download_media(
                bb,
                "./resources/downloads/",
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(
                        d,
                        t,
                        xx,
                        ccc,
                        "Downloading...",
                    )
                ),
            )
        else:
            return await eod(xx, "`Reply to media file`", time=5)
    try:
        results = await Ultra_bot.inline_query(
            Var.BOT_USERNAME, f"fl2lnk {file_name}"
        )
    except rep:
        return await eor(
            xx,
            "`The bot did not respond to the inline query.\nConsider using {}restart`".format(
                HNDLR
            ),
        )
    except dis:
        return await eor(
            xx, "`Please turn on inline mode for your bot from` @Botfather."
        )
    await results[0].click(event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True)
    await xx.delete()
    await event.delete()


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
