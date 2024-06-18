import asyncio
import sys
from pyrogram import Client, errors
from Pokemonxd.utilities import config
from Pokemonxd.console import LOGGER

class Bot(Client):
    def __init__(self):
        LOGGER(__name__).info("🥀 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 💞...")
        super().__init__(
            "Pokemonxd",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.name = f"{get_me.first_name} {get_me.last_name}" if get_me.last_name else get_me.first_name
        self.username = get_me.username
        self.id = get_me.id
        
        log_message = (
            f"**━━━━━━━━━━━━━━━━━━━**\n"
            f"**✅ 𝐁𝐨𝐭 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 🥳**\n"
            f"**━━━━━━━━━━━━━━━━━━━**\n"
            f"**🥀 𝐍𝐚𝐦𝐞 ›** {self.name}\n"
            f"**🌸 𝐋𝐢𝐧𝐤 : ›** @{self.username}\n"
            f"**🌷 𝐈𝐃✩ : ›** `{self.id}`\n"
            f"**━━━━━━━━━━━━━━━━━━━**\n"
            f"**🔥 𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 : [𝐏𝐨𝐤𝐞𝐦𝐨𝐧 𝐒𝐞𝐫𝐯𝐞𝐫](https://t.me/Tc_pokemon).**\n"
            f"**━━━━━━━━━━━━━━━━━━━**"
        )

        try:
            await self.send_message_with_retry(
                config.LOG_GROUP_ID,
                log_message,
                disable_web_page_preview=True
            )
        except Exception as e:
            LOGGER(__name__).error(f"Failed to send start message: {e}")

    async def send_message_with_retry(self, chat_id, text, disable_web_page_preview):
        retries = 5
        for i in range(retries):
            try:
                await self.send_message(chat_id, text, disable_web_page_preview=disable_web_page_preview)
                break
            except errors.BadMsgNotification as e:
                if e.x == 16:
                    LOGGER(__name__).warning(
                        f"BadMsgNotification error (attempt {i+1}/{retries}): {e}. Retrying in {5 * (i+1)} seconds..."
                    )
                    await asyncio.sleep(5 * (i+1))  # Exponential backoff
                else:
                    raise

if __name__ == "__main__":
    bot = Bot()
    bot.run()
    
