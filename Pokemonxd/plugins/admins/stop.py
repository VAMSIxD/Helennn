from pyrogram import filters
from pyrogram.types import Message

from Pokemonxd import bot
from Pokemonxd.utilities.config import BANNED_USERS
from Pokemonxd.utilities.strings import get_command
from Pokemonxd.utilities.events.command import command
from Pokemonxd.modules.core.call import poke
from Pokemonxd.modules.database import set_loop
from Pokemonxd.modules.decorators import AdminRightsCheck

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@bot.on_message(
    command(STOP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await poke.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_9"].format(message.from_user.mention)
    )
