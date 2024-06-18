from pyrogram import filters
from pyrogram.types import Message

from Pokemonxd.utilities.config import BANNED_USERS
from Pokemonxd.utilities.strings import get_command
from Pokemonxd.utilities.events.command import command
from Pokemonxd import bot
from Pokemonxd.modules.core.call import poke
from Pokemonxd.modules.database import is_music_playing, music_on
from Pokemonxd.modules.decorators import AdminRightsCheck

# Commands
RESUME_COMMAND = get_command("RESUME_COMMAND")


@bot.on_message(
    command(RESUME_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if message.edit_date:
        return  # Skip processing if the message has been edited
    
    if len(message.command) != 1:
        return await message.reply_text(_["general_2"])
    
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    
    await music_on(chat_id)
    await poke.resume_stream(chat_id)
    
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention)
    )
