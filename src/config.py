import json
import os


def get_user_list(config, key):
    with open("{}/src/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 10872193  # integer value, dont use ""
    API_HASH = "7a2c777e52479d13fb1adb29944130cf"
    TOKEN = "5699376101:AAGtSMEy8LgqixXw2RV-Blyh7B_ZI-FCako"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 5205602399  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "MolesteRishu"
    SUPPORT_CHAT = "ShanksxDoffy_support"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001659204080
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001659204080
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    MONGO_DB_URI = "mongodb+srv://xelcius:raizel~97@cluster0.gj9j8.mongodb.net/cluster0?retryWrites=true&w=majority"
    STRING_SESSION = "1BVtsOHQBu5YRMvuQOZWv-pFXDpfhj5_c33vo3kssCg9VhG1sneBdHC8wVbAiBg__1LbxTrJ3gYSQk-Ff6f5iyK0ZFlYz3oMwjXz-7R9goCJ5BcU-pA48T2YXaoKwmXiczE6_b14esmMqLfqQZ8gf1Ws1dFvZM77kk57jFDceiwPRqN_0YugxmQzRp6mS73OMRRFhuWBGJIURftwup7gSTYs25-8D2BUvjbp3AboBomapf7KgxeJ7e4rfQ_eoV0MXtTEjcBW39nESS0mcfG0jyO_XDNF7THuIGnZYj9SvhuWN7OHKve4NDpNLrsJpVObFCFPcStrGnuTcL3QQmFUe527P5EJeLWY="
    ARQ_API_KEY = "HRINZL-XDAQVW-AZYEPT-ZZJZSH-ARQ"
    SQLALCHEMY_DATABASE_URI = "postgres://ixpzecqk:5z6H-w2aq3hp4rRfMES-Ehinta3mUY37@suleiman.db.elephantsql.com/ixpzecqk"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS =  get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS =  get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "6950f559377140a4e1594c564cdca6a3"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None

 ALLOW_CHATS = [] 
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
    ALLOW_CHATS = [] 
