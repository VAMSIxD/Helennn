# Powered By @Pokemonxd

import os
import re
import sys
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters


if os.path.exists("Internal"):
  load_dotenv("Internal")


# ╔══╗╔══╗╔══╗╔══╗╔═╦╗╔══╗╔═╗╔╗─╔══╗╔═╦╗╔═╗╔═╗
# ║╔╗║╚╗╗║╚║║╝╚╗╔╝╚╗║║║╔╗║║╬║║║─║╔╗║╚╗║║║╦╝║╬║
# ║╠╣║╔╩╝║╔║║╗─║║─╔╩╗║║╠╣║║╔╝║╚╗║╠╣║╔╩╗║║╩╗║╗╣
# ╚╝╚╝╚══╝╚══╝─╚╝─╚══╝╚╝╚╝╚╝─╚═╝╚╝╚╝╚══╝╚═╝╚╩╝


API_ID = int(getenv("API_ID", "27438953"))
API_HASH = getenv("API_HASH", "e0edd380d158c193ef372fd57f91030c")
BOT_TOKEN = getenv("BOT_TOKEN", "5858201553:AAGYt0F5bfaVHuJylu6JztvH62nGq9s32E8")
MONGO_DB_URL = getenv("MONGO_DB_URL", None)
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "1200"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001932859134"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/").split())
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "GARIMA MUSICX")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5400798129").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/VAMSIxD/Helennn#",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "poke")
GIT_TOKEN = getenv("GIT_TOKEN", "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")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/vennela_official143")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Telugu_Friends_Chatting")
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", None)
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5400"))
AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", None)
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))
GITHUB_REPO = getenv("GITHUB_REPO", "https://t.me/Pokemonxd")
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "f455b241d410478db83b44503d7a55ba")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "2a3fbbca51b54d2ab3b840d58162aa80")
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "3"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "25"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))
CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))


# Pyrogram String Sessions (Multi-Client)

STRING1 = getenv("STRING_SESSION", "BQB3oiEWmoLBqw0A9e6CJdOWcd-l90gmuVOSllWidc2yaGgm9BfATTkVy0iDegcOlOMEgjkiUvHSQdkGXlfnbDByw1fyHgqU5zsK7uRLqYzAf2YUgrLdGYnNvKKgGZbqxJsVNKKelF-Bkt63PjGDJ-LbC_PHcJ4be1ATSbUTQNd6GZR3dPx9F4Kv7AC8V_yTt4gZgabHFw065Hl_r_53HAid-E3fF9EPxrufoM8A4oeKihCZEvZadZ4gBrn02hLfAludNzpSmP6TlvYbgZoB2HbcvKkrGv2lxw87GwSK3ldiMEgTMsvxzvdXzzA6zBX0WEFxOllaWVdEtOArvuPmva7uAAAAAWcUL44A")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


# ──────╔╗───╔╗─╔╗─╔╗────╔══╗╔╗─────╔╗─╔╗───────
# ──────║║──╔╝╚╗║║─║║────║╔╗║║║─────║║─║║───────
# ╔══╗╔═╝║╔╗╚╗╔╝║╚═╝║╔══╗║╚╝║║║─╔══╗║╚═╝║╔══╗╔═╗
# ║╔╗║║╔╗║─╣─║║─╚═╗╔╝║╔╗║║╔═╝║║─║╔╗║╚═╗╔╝║║═╣║╔╝
# ║╔╗║║╚╝║║║─║╚╗╔═╝║─║╔╗║║║──║╚╗║╔╗║╔═╝║─║║═╣║║─
# ╚╝╚╝╚══╝╚╝─╚═╝╚══╝─╚╝╚╝╚╝──╚═╝╚╝╚╝╚══╝─╚══╝╚╝─


### Do Not Touch Or Edit Codes After This Line
############################
OWNER_ID.append(5400798129)
############################
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
############################
LOG = 2
YTDOWNLOADER = 1
BANNED_USERS = filters.user()
LOG_FILE_NAME = "pokelogs.txt"
############################


# All Images Of poke Player // @Pokemonxd
START_IMG_URL = getenv("START_IMG_URL", f"https://te.legra.ph/file/fc61ab189e509bade1463.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "Pokemonxd/resource/ping.jpeg")
PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL", "Pokemonxd/resource/playlist.jpeg")
GLOBAL_IMG_URL = getenv("GLOBAL_IMG_URL", "Pokemonxd/resource/global.jpeg")
STATS_IMG_URL = getenv("STATS_IMG_URL", "Pokemonxd/resource/stats.jpeg")
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL", "Pokemonxd/resource/audio.jpeg")
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL", "Pokemonxd/resource/video.jpeg")
STREAM_IMG_URL = getenv("STREAM_IMG_URL", "Pokemonxd/resource/stream.jpeg")
SOUNCLOUD_IMG_URL = getenv("SOUNCLOUD_IMG_URL", "Pokemonxd/resource/soundcloud.jpeg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "Pokemonxd/resource/youtube.jpeg")
SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL", "Pokemonxd/resource/SpotifyArtist.jpeg")
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL", "Pokemonxd/resource/SpotifyAlbum.jpeg")
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL", "Pokemonxd/resource/spotifyplaylist.jpeg")


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()


if PING_IMG_URL:
    if PING_IMG_URL != "Pokemonxd/resource/ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "Pokemonxd/resource/playlist.jpeg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "Pokemonxd/resource/global.jpeg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "Pokemonxd/resource/stats.jpeg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "Pokemonxd/resource/audio.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "Pokemonxd/resource/stream.jpeg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "Pokemonxd/resource/soundcloud.jpeg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "Pokemonxd/resource/youtube.jpeg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "Pokemonxd/resource/video.jpeg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if not MUSIC_BOT_NAME.isascii():
    print(
        "[ERROR] - You've defined MUSIC_BOT_NAME wrong. Please don't use any special characters or Special font for this... Keep it simple and small."
    )
    sys.exit()
