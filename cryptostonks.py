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
# ⚠️ Owner @morri_py, @morri_bio
# ---------------------------------------------------------------------------------
# meta developer: @morri_py
import requests

from .. import loader, utils

__version__ = (1, 0, 0)

@loader.tds
class CryptoStonksMod(loader.Module):
    """Show Stonks"""

    strings = {
        "name": "CryptoStonks",
        "who": "<emoji document_id=5280842756367851322>📈</emoji> Cryptocurrency exchange rate",
    }

    strings_ru = {
        "who": "<emoji document_id=5280842756367851322>📈</emoji> Курс криптовалюты",
    }

    strings_uk = {
        "who": "<emoji document_id=5280842756367851322>📈</emoji> Курс криптовалюти",
    }

    async def stonks(self, symbols):
        url = "https://min-api.cryptocompare.com/data/pricemulti"
        parameters = {
            "fsyms": symbols,
            "tsyms": "USD,EUR,RUB,UAH",
            "api_key": "5d4d8c117119d62fae3290bb0587a20af7e2768c237df3690ce8bab4111b7330"
        }
        try:
            response = requests.get(url, params=parameters)
            response.raise_for_status()
            data = response.json()

            result = f"<b>{self.strings['who']}</b>\n\n"
            for symbol in symbols.split(","):
                price = data[symbol]
                if symbol == "BTC":
                    emoji = "<emoji document_id=5465465383035083768>🪙</emoji>"
                elif symbol == "TON":
                    emoji = "<emoji document_id=5197515039296200279>💎</emoji>"
                elif symbol == "ETH":
                    emoji = "<emoji document_id=5458702441631456730>🪩</emoji>"
                elif symbol == "USDT":
                    emoji = "<emoji document_id=5465546600866652008>💰</emoji>"    
                else:
                    emoji = ""
                result += f"{emoji} 1 {symbol}:\n\n"
                result += f"<emoji document_id=6323139226418284334>🇷🇺</emoji> {price['RUB']:.2f} RUB\n"
                result += f"<emoji document_id=6323374027985389586>🇺🇸</emoji> {price['USD']:.2f} USD\n"
                result += f"<emoji document_id=6323217102765295143>🇪🇺</emoji> {price['EUR']:.2f} EUR\n"
                result += f"<emoji document_id=6323289850921354919>🇺🇦</emoji> {price['UAH']:.2f} UAH\n\n"

        except Exception as e:
            result = f"An error occurred while getting prices: {str(e)}"

        return result
    
    @loader.command(
        ru_doc="Показать курс BTC",
        ua_doc="Показати курс BTC"
    )
    async def btccmd(self, message):
        """Show BTC stonks"""
        result = await self.stonks("BTC")
        await utils.answer(message, result)

    @loader.command(
        ru_doc="Показать курс TON",
        ua_doc="Показати курс TON"
    )
    async def sttoncmd(self, message):
        """Show TON stonks"""
        result = await self.stonks("TON")
        await utils.answer(message, result)

    @loader.command(
        ru_doc="Показать курс ETH",
        ua_doc="Показати курс ETH"
    )
    async def stethcmd(self, message):
        """Show ETH stonks"""
        result = await self.stonks("ETH")
        await utils.answer(message, result)

    @loader.command(
        ru_doc="Показать курс USDT",
        ua_doc="Показати курс USDT"
    )
    async def stusdtcmd(self, message):
        """Show USDT stonks"""
        result = await self.stonks("USDT")
        await utils.answer(message, result)

    @loader.command(
        ru_doc="Показать курс всех криптовалют (которые в модуле)",
        ua_doc="Показати курс всіх криптовалюта (які в модулі)"
    )
    async def stcryptocmd(self, message):
        """Show all stonks"""
        result = await self.stonks("BTC,TON,ETH,USDT")
        await utils.answer(message, result)
