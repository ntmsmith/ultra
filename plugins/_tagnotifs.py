from telethon import custom, events
from telethon.utils import get_display_name

from . import *


@Ultra_bot.on(
    events.NewMessage(
        incoming=True,
        func=lambda e: (e.mentioned),
    )
)
async def all_messages_catcher(e):
    if udB.get("TAG_LOG") is not None:
        NEEDTOLOG = int(udB.get("TAG_LOG"))
        x = await Ultra_bot.get_entity(e.sender_id)
        if x.bot:
            return
        y = await Ultra_bot.get_entity(e.chat_id)
        xx = f"[{get_display_name(x)}](tg://user?id={x.id})"
        yy = f"[{get_display_name(y)}](https://t.me/c/{y.id})"
        msg = f"https://t.me/c/{y.id}/{e.id}"
        if e.text:
            cap = f"{xx} tagged you in {yy}\n\n```{e.text}```\nㅤ"
        else:
            cap = f"{xx} tagged you in {yy}"
        btx = "📨 View Message"
        try:
            await asst.send_message(
                NEEDTOLOG,
                cap,
                link_preview=False,
                buttons=[[custom.Button.url(btx, msg)]],
            )
        except BaseException:
            if e.text:
                cap = get_string("tagnot_1").format(xx, yy, e.text, msg)
            else:
                cap = get_string("tagnot_2").format(xx, yy, msg)
            try:
                await Ultra_bot.send_message(NEEDTOLOG, cap, link_preview=False)
            except BaseException:
                pass
    else:
        return
