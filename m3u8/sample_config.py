import os


class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6135772410:AAHvOnKtVflG23aAKupNtZeQLjvDvsJavuI")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 7978114))
    API_HASH = os.environ.get("API_HASH", "5f7839feeba133497f24acfd005ef2ec")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1760280598").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    CHUNK_SIZE = 128
    PROCESS_MAX_TIMEOUT = 3600
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get(
        "DEF_THUMB_NAIL_VID_S",
        "https://placehold.it/90x90"
    )
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from
    # https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", None)
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "░")
    BLACKLIST_USERS = set(int(x) for x in os.environ.get("BLACKLIST_USERS", "").split())
    # Database url
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Multi:MultiBot@mutlti.9wqqaki.mongodb.net/?retryWrites=true&w=majority")
