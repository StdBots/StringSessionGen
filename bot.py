from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    FORCE_SUB_CHANNEL,
    CHANNEL_LINK,
    SUPPORT_LINK
)

app = Client(
    "StringSessionGenBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


async def is_subscribed(client, user_id):
    try:
        await client.get_chat_member(FORCE_SUB_CHANNEL, user_id)
        return True
    except UserNotParticipant:
        return False
    except Exception:
        return False


@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    if not await is_subscribed(client, message.from_user.id):
        await message.reply(
            "🔒 **Join our channel to use this bot**\n\nAfter joining, click **Try Again** 👇",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)],
                    [InlineKeyboardButton("🔄 Try Again", callback_data="recheck")]
                ]
            )
        )
        return

    await message.reply(
        f"""
━━━━━━━━━━━━━━━━━━
🤖 STRING SESSION BOT
━━━━━━━━━━━━━━━━━━

👋 Hey {message.from_user.first_name}!

Generate Telegram string sessions
quickly using a modern web interface.

✨ Supported:
• API ID $ API HASH 
• Pyrogram 
• Telethon

⚡ Fast • Safe • Secure
━━━━━━━━━━━━━━━━━━
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⚙️ Generate Session", callback_data="generate")],
                [
                    InlineKeyboardButton("📢 Channel", url=CHANNEL_LINK),
                    InlineKeyboardButton("🆘 Support", url=SUPPORT_LINK)
                ]
            ]
        )
    )


@app.on_callback_query(filters.regex("recheck"))
async def recheck(client, callback):
    if not await is_subscribed(client, callback.from_user.id):
        await callback.answer("❌ Please join the channel first!", show_alert=True)
        return

    await callback.message.delete()
    await start(client, callback.message)


@app.on_callback_query(filters.regex("generate"))
async def generate(client, callback):
    await callback.message.reply(
        """
━━━━━━━━━━━━━━━━━━
🔐 GENERATE STRING SESSION
━━━━━━━━━━━━━━━━━━

You will need:
• Telegram API ID
• Telegram API HASH

Choose an option 👇
━━━━━━━━━━━━━━━━━━
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🔑 Create API ID & HASH", url="https://my.telegram.org/auth")],
                [InlineKeyboardButton("🐍 Pyrogram Session", url="https://telegram.tools/session-string-generator#pyrogram,user")],
                [InlineKeyboardButton("📡 Telethon Session", url="https://telegram.tools/session-string-generator#telethon,user")]
            ]
        )
    )
    await callback.answer()


app.run()
