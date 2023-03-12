# 🔒 The GPL-3.0 license
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
#
# ---------------------------------------------------------------------------------
#⠄⠄⠄⠄⡠⣿⢷⣻⣿⣾⣳⡇⢺⠟⠒⠒⠶⢤⣈⠃⢠⡀
#⠄⠄⠄⢀⣼⡿⠋⢉⣉⣙⠿⠁⢁⣤⣤⣄⡀⠄⠈⠳⢾⣿⣄
#⠄⠄⠄⢞⡞⠄⣴⣿⡿⠛⠓⠄⠉⠉⠉⠉⠹⣷⣄⠄⠄⠙⢿⣦
#⠄⢀⣾⡟⠄⣸⠟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢿⡀⠄⠰⣿⣆
#⠄⢸⣿⠁⢸⣿⠄⠄⢸⢸⠄⠄⠄⢸⣆⢠⣀⡀⣧⣨⣻⡀⠄⢻⣿⣦⣀
#⠄⢸⡇⡀⠘⣿⢰⣐⢾⢿⡀⠄⡀⢨⣎⣻⣷⣶⣿⣿⣿⣇⢀⢸⣿⣿⣿⣷
#⠄⢸⣣⡇⣧⣿⣿⣿⣿⡎⢳⣟⠿⣿⣿⣏⣉⣿⣿⣿⢻⣿⣿⣾⣿⣿⣿⣿⣦
#⠄⠄⢼⡇⢹⣿⡏⢠⣿⣿⠄⠉⠄⠄⠈⠄⢹⣿⠟⠼⢻⣿⣿⣿⣿⣿⣿⣿⣿
#⠄⠄⠈⢿⢈⣿⡛⠘⣿⡇⠄⠄⡀⠄⠄⠄⠈⠉⠁⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿
#⠄⠄⢀⣿⣼⡿⣿⣀⠄⠄⠄⠄⠃⠄⠄⠄⠄⠄⠄⠘⣻⡏⣿⣿⢻⣿⣿⣿⣿
#⠄⠄⠾⢻⡇⣿⣸⣦⣀⠄⠄⠐⢟⠙⢻⠃⠄⠄⠄⣾⡏⣷⢻⡹⡟⣿⣿⡟⢿
#⠄⢀⡴⢻⣇⢿⣷⢻⡟⠻⣶⣤⣀⠉⠄⣀⣴⡿⢣⡟⠄⣿⢸⡇⣰⡟⠻⠃⢸
#⢠⡏⠄⠄⠈⠻⣿⣏⣷⠄⠈⠻⠉⠛⠛⠉⠄⠄⢛⠄⠄⠻⢠⠁⢛⠁⠄⠄⢸
#⣼⠄⠄⠄⠄⠄⠈⢿⡘⠃⠄⠄⠄⠄⠄⠄⠠⠈⠄⠄⠄⢠⣸⣠⡞⠄⠄⠄⣿
#⣤⠄⠄⠄⠄⠄⠄⢸⣇⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⣿⠟⠄⠄⠄⣸⣿
#
# 👾 Module for Telethon User Bot (Netfoll, Hikka, FTG)
# 🔒 The GPL-3.0 license
# ⚠️ Owner @morri_py, @morri_bio, @amoremods
# All rights reserved > @aewakatimebot
# ---------------------------------------------------------------------------------
# meta developer: @morri_py, @amoremods

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from .. import loader, utils
__version__ = (1, 0, 0)

@loader.tds
class WakaInfoMod(loader.Module):
    """WakaTime info - @aewakatimebot"""

    strings = {
        "name": "WakaInfo",
        "banned": "🚫 <b>Unban @aewakatimebot</b>",
    }
    
    strings_ru = {
        "banned": "🚫 <b>Разблокируй @aewakatimebot</b>",
    }
        
    strings_uk = {
        "banned": "🚫 <b>Розблокувавши @aewakatimebot</b>",
    }
    
    async def wakacmd(self, message):
        """Show Info WakaTime"""
        waka = "/waka"
        chat = "@aewakatimebot"
        async with message.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=5518933800)
                )
                wakainfo = await conv.send_message(waka)
                response = await response
                await utils.answer(message, response.text)
                await response.delete()
                await wakainfo.delete()
            except YouBlockedUserError:
                return await message.reply(message, self.strings("banned"))