import random

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

from Pokemonxd.utilities.config import BANNED_USERS
from Pokemonxd.utilities.strings import get_command
from Pokemonxd import bot, YouTube
from Pokemonxd.misc import db
from Pokemonxd.modules.decorators import AdminRightsCheck
from Pokemonxd.modules.core.call import poke
from Pokemonxd.modules.stream.autoclear import auto_clean
from Pokemonxd.modules.utils.thumbnails import gen_thumb

# Commands
SKIP_COMMAND = get_command("SKIP_COMMAND")

# Command handler
@bot.on_message(
    filters.command(SKIP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def skip(cli, message: Message, _, chat_id):
    if not len(message.command) < 2:  # Check if exactly one argument is provided
        return await message.reply_text(_["general_2"])
    
    check = db.get(chat_id)  # Retrieve current queue from the database
    if not check:
        return await message.reply_text(_["queue_2"])  # Handle empty queue
    
    try:
        state = int(message.text.split(None, 1)[1].strip())  # Get skip number
    except ValueError:
        return await message.reply_text(_["admin_13"])  # Handle non-numeric argument
    
    if state <= 0 or state > len(check):
        return await message.reply_text(_["admin_15"].format(len(check)))  # Handle out-of-range skip
    
    # Process the skip command
    for _ in range(state):
        popped = check.pop(0)
        if popped:
            if config.AUTO_DOWNLOADS_CLEAR == str(True):
                await auto_clean(popped)  # Optional: Clean up resources if configured
            
    if not check:
        try:
            await poke.stop_stream(chat_id)
        except:
            pass
        
        return await message.reply_text(_["admin_10"].format(message.from_user.first_name))
    
    queued = check[0]["file"]
    title = check[0]["title"].title()
    user = check[0]["by"]
    streamtype = check[0]["streamtype"]
    videoid = check[0]["vidid"]
    status = True if str(streamtype) == "video" else None
    
    if "live_" in queued:
        n, link = await YouTube.video(videoid, True)
        if n == 0:
            return await message.reply_text(_["admin_11"].format(title))
        
        try:
            await poke.skip_stream(chat_id, link, video=status)
        except Exception:
            return await message.reply_text(_["call_9"])
        
        button = telegram_markup(_, chat_id)
        img = await gen_thumb(videoid)
        run = await message.reply_photo(
            photo=img,
            caption=_["stream_1"].format(
                user,
                f"https://t.me/{bot.username}?start=info_{videoid}",
            ),
            reply_markup=InlineKeyboardMarkup(button),
        )
        db[chat_id][0]["mystic"] = run
        db[chat_id][0]["markup"] = "tg"
    
    elif "vid_" in queued:
        mystic = await message.reply_text(_["call_10"], disable_web_page_preview=True)
        
        try:
            file_path, direct = await YouTube.download(
                videoid,
                mystic,
                videoid=True,
                video=status,
            )
        except:
            return await mystic.edit_text(_["call_9"])
        
        try:
            await poke.skip_stream(chat_id, file_path, video=status)
        except Exception:
            return await mystic.edit_text(_["call_9"])
        
        button = stream_markup(_, videoid, chat_id)
        img = await gen_thumb(videoid)
        run = await message.reply_photo(
            photo=img,
            caption=_["stream_1"].format(
                user,
                f"https://t.me/{bot.username}?start=info_{videoid}",
            ),
            reply_markup=InlineKeyboardMarkup(button),
        )
        db[chat_id][0]["mystic"] = run
        db[chat_id][0]["markup"] = "stream"
        await mystic.delete()
    
    elif "index_" in queued:
        try:
            await poke.skip_stream(chat_id, videoid, video=status)
        except Exception:
            return await message.reply_text(_["call_9"])
        
        button = telegram_markup(_, chat_id)
        run = await message.reply_photo(
            photo=config.STREAM_IMG_URL,
            caption=_["stream_2"].format(user),
            reply_markup=InlineKeyboardMarkup(button),
        )
        db[chat_id][0]["mystic"] = run
        db[chat_id][0]["markup"] = "tg"
    
    else:
        try:
            await poke.skip_stream(chat_id, queued, video=status)
        except Exception:
            return await message.reply_text(_["call_9"])
        
        if videoid == "telegram":
            button = telegram_markup(_, chat_id)
            run = await message.reply_photo(
                photo=config.TELEGRAM_AUDIO_URL if str(streamtype) == "audio"
                else config.TELEGRAM_VIDEO_URL,
                caption=_["stream_3"].format(title, check[0]["dur"], user),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
        
        elif videoid == "soundcloud":
            button = telegram_markup(_, chat_id)
            run = await message.reply_photo(
                photo=config.SOUNCLOUD_IMG_URL if str(streamtype) == "audio"
                else config.TELEGRAM_VIDEO_URL,
                caption=_["stream_3"].format(title, check[0]["dur"], user),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
        
        else:
            button = stream_markup(_, videoid, chat_id)
            img = await gen_thumb(videoid)
            run = await message.reply_photo(
                photo=img,
                caption=_["stream_1"].format(
                    user,
                    f"https://t.me/{bot.username}?start=info_{videoid}",
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "stream"
