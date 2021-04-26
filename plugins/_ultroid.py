from telethon.errors import ChatSendInlineForbiddenError

from . import *

REPOMSG = (
    "• **Ultra USERBOT** •\n\n",
    "• Repo - [Click Here](https://github.com/TeamUltra/Ultra)\n",
    "• Support - @UltraSupport",
)


@Ultra_cmd(pattern="repo$")
async def repify(e):
    try:
        q = await Ultra_bot.inline_query(Var.BOT_USERNAME, "repo")
        await q[0].click(e.chat_id)
        if e.sender_id == Ultra_bot.uid:
            await e.delete()
    except ChatSendInlineForbiddenError:
        await eor(e, REPOMSG)
