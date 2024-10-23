# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# List of user IDs that are allowed to access the commands
ALLOWED_USER_IDS = {50700752896289965347,}  # Replace with actual user IDs

def check_user(update: Update) -> bool:
    """Check if the user is in the allowed list."""
    return update.effective_user.id in ALLOWED_USER_IDS

def start(update: Update, context: CallbackContext) -> None:
    if check_user(update):
        update.message.reply_text("Welcome! You can use the commands /txt, /upload, /stop.")
    else:
        update.message.reply_text("You are not authorized to use this bot.")

def txt(update: Update, context: CallbackContext) -> None:
    if check_user(update):
        update.message.reply_text("This is the /txt command response.")
    # No else block means no response if the user is not authorized.

def upload(update: Update, context: CallbackContext) -> None:
    if check_user(update):
        update.message.reply_text("This is the /upload command response.")
    
def stop(update: Update, context: CallbackContext) -> None:
    if check_user(update):
        update.message.reply_text("This is the /stop command response.")

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("txt", txt))
    dispatcher.add_handler(CommandHandler("upload", upload))
    dispatcher.add_handler(CommandHandler("stop", stop))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop (Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()







import time
import math
import os
from pyrogram.errors import FloodWait

class Timer:
    def __init__(self, time_between=5):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False


from datetime import datetime,timedelta

def hrb(value, digits= 2, delim= "", postfix=""):
    """Return a human-readable file size.
    """
    if value is None:
        return None
    chosen_unit = "B"
    for unit in ("KiB", "MiB", "GiB", "TiB"):
        if value > 1000:
            value /= 1024
            chosen_unit = unit
        else:
            break
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix

def hrt(seconds, precision = 0):
    """Return a human-readable time delta as a string.
    """
    pieces = []
    value = timedelta(seconds=seconds)
    

    if value.days:
        pieces.append(f"{value.days}d")

    seconds = value.seconds

    if seconds >= 3600:
        hours = int(seconds / 3600)
        pieces.append(f"{hours}h")
        seconds -= hours * 3600

    if seconds >= 60:
        minutes = int(seconds / 60)
        pieces.append(f"{minutes}m")
        seconds -= minutes * 60

    if seconds > 0 or not pieces:
        pieces.append(f"{seconds}s")

    if not precision:
        return "".join(pieces)

    return "".join(pieces[:precision])



timer = Timer()

async def progress_bar(current, total, reply, start):
    if timer.can_send():
        now = time.time()
        diff = now - start
        if diff < 1:
            return
        else:
            perc = f"{current * 100 / total:.1f}%"
            elapsed_time = round(diff)
            speed = current / elapsed_time
            remaining_bytes = total - current
            if speed > 0:
                eta_seconds = remaining_bytes / speed
                eta = hrt(eta_seconds, precision=1)
            else:
                eta = "-"
            sp = str(hrb(speed)) + "/s"
            tot = hrb(total)
            cur = hrb(current)
            bar_length = 11
            completed_length = int(current * bar_length / total)
            remaining_length = bar_length - completed_length
            progress_bar = "▰" * completed_length + "▱" * remaining_length
            
            try:
                await reply.edit(f'<b>\n ╭──⌯════🆄︎ᴘʟᴏᴀᴅɪɴɢ⬆️⬆️═════⌯──╮ \n├⚡ {progress_bar}|﹝{perc}﹞ \n├🚀 Speed » {sp} \n├📟 Processed » {cur}\n├🧲 Size - ETA » {tot} - {eta} \n├🤖 𝔹ʏ » @FsgNation\n╰─═══@FsgNation🍃═══─╯\n</b>') 
            except FloodWait as e:
                time.sleep(e.x)

