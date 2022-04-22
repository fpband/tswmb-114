# (c) @FarshidBand

import time
from humanfriendly import format_timespan
from configs import Config
from core.display_progress import progress_for_pyrogram, humanbytes
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def send_video_handler(bot, cmd, output_vid, video_thumbnail, duration, width, height, editable, logs_msg, file_size):
    c_time = time.time()
    sent_vid = await bot.send_video(
        chat_id=cmd.chat.id,
        video=output_vid,
        caption=f"**• File Name:** `{output_vid}`\n**• Video Duration:** `{format_timespan(duration)}`\n**• File Size:** `{humanbytes(file_size)}`\n\n{Config.CAPTION}",
        thumb=video_thumbnail,
        duration=duration,
        width=width,
        height=height,
        reply_to_message_id=cmd.message_id,
        supports_streaming=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✍️ ارسال نظرات و پیشنهادات ⁦❤️⁩", url="https://t.me/FarshidBand")],
                                           [InlineKeyboardButton("🔮 کانال پشتیبانی", url="https://t.me/SeriesPlus1"),
                                            InlineKeyboardButton("🔮 گروه پشتیبانی", url="https://t.me/dlchinhub")]]),
        progress=progress_for_pyrogram,
        progress_args=(
            "**📤 در حال آپلود ویدیو ...**",
            editable,
            logs_msg,
            c_time
        )
    )
    return sent_vid
