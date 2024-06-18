from pyrogram import filters
from pyrogram.types import Message

from Pokemonxd.utilities.config import BANNED_USERS
from Pokemonxd.utilities.strings import get_command
from Pokemonxd import bot
from Pokemonxd.modules.core.call import poke
from Pokemonxd.modules.database import is_muted, mute_on
from Pokemonxd.modules.decorators import AdminRightsCheck

# Commands
MUTE_COMMAND = get_command("MUTE_COMMAND")


@bot.on_message(
    filters.command(MUTE_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    if message.edit_date:
        return  # Skip processing if the message has been edited
    
    if len(message.command) != 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    
    if await is_muted(chat_id):
        return await message.reply_text(_["admin_5"])
    
    await mute_on(chat_id)
    await poke.mute_stream(chat_id)
    await message.reply_text(
        _["admin_6"].format(message.from_user.mention)
    )
    
