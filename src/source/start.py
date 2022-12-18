import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from src.events import register
from src import telethn as tbot

VENOM = "https://telegra.ph/file/52715f72b6d72144e5790.mp4"

@register(pattern=("/start"))
async def awake(event):
  TEXT = f"""Heya [{event.sender.first_name}](tg://user?id={event.sender.id}),やあ  "How did I end up following a Captain like this"
I am Shanks, also known as "Red Haired Shanks", I am The captain of The Red Hair Pirates.
Now That You Pointed The Gun, Would You Risk Your Life For It?!.\n\n"""
  TEXT += "Join Our [Chat Group](https://t.me/Void_ivq) to chat about anime and stuff."
  BUTTON = [[Button.url("➕Add Me To Your Group➕", "https://t.me/Shanksrobot?startgroup=true"),]]
  await tbot.send_file(event.chat_id, VENOM, caption=TEXT, buttons=BUTTON)
