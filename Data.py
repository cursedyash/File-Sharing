# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ commands for users
 ├ /start - start me 
 ├ /about - about
 ├ /help - commands for this bot
 ├ /ping - check if i am active or not 
 └ /uptime - time status of bot 
 
 ❏ commands for admins 
 ├ /logs - to check the logs 
 ├ /setvar - to set a variable
 ├ /delvar - to delete the variable
 ├ /getvar - to view the variable using this command 
 ├ /users - to check how many users are using this bot
 ├ /batch - to generate mulitple file link
 ├ /speedtest - to check the server speed 
 └ /broadcast - to broadcaste message

Develoved by </b><a href='https://t.me/apatheticyash'>@apatheticyash</a>
"""

    close = [
        [InlineKeyboardButton("close", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("close", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("About", callback_data="about"),
            InlineKeyboardButton("close", callback_data="close")
        ],
    ]

    ABOUT = """
<b>about this bot:

@{} telegram bot saving and storing files which can be accessed through special links.

 • Creator: @{}
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 

Develoved by </b><a href='https://t.me/apatheticyash'>@apatheticyash</a>
"""
