""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.mhelp$")
async def usit(e):
    await e.edit(
        f"      ╔════════════╗\n     **__⚡️BANTUAN⚡️__**     \n╚════════════╝ \n"
        f"**Hai Remix {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "═⎆ developer  : [hacker](t.me/FlashProSpeed) \n"
        "═⎆ Repository : [Remix-Userbot](https://github.com/Randi356/Remix-Userbot) \n"
        "═⎆ Instragam  : [Instagram Yotteno](Instagram.com/yotteno) \n"
        "═⎆ Grup Support : [Remix Userbot Support](https://t.me/StaryWild)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"      ╔════════════╗\n  **__⚡️DAFTAR VARS⚡️__**     \n╚════════════╝ \n"
        f"**Disini Daftar Vars Dari King** {DEFAULTUSER} :\n"
        "═⎆ Daftar Vars : [DAFTAR VARS](https://raw.githubusercontent.com/Randi356/Remix-Userbot/Remix-Userbot/varshelper.txt)")


CMD_HELP.update(
    {
        "helper": "**✘ Plugin :** `Helper`\
        \n\n  •  **Perintah :** `.mhelp`\
        \n  •  **Function : **Bantuan Untuk ⚡️𝙍𝙚𝙢𝙞𝙭-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡️\
        \n\n  •  **Perintah :** `.vars`\
        \n  •  **Function : **Melihat Daftar Vars\
    "
    }
)
