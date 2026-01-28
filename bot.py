from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

from config import API_ID, API_HASH, BOT_TOKEN, FORCE_SUB_CHANNEL, SUPPORT_LINK, CHANNEL_LINK

app = Client(
    "StringSessionGenBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


# 🔒 FORCE SUBSCRIBE CHECK
async def force_subscribe(client, message):
    try:
        await client.get_chat_member(FORCE_SUB_CHANNEL, message.from_user.id)
        return True
    except UserNotParticipant:
        return False
    except Exception:
        return False


# 🚀 START COMMAND
@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    is_joined = await force_subscribe(client, message)

    if not is_joined:
        await message.reply(
            "🔒 **Join our channel to use this bot**\n\n"
            "After joining, press **Try Again** 👇",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)
                    ],
                    [
                        InlineKeyboardButton("🔄 Try Again", callback_data="check_sub")
                    ]
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

I help you generate Telegram
string sessions quickly and easily.

✨ Supported Clients
• Pyrogram (v1 / v2)
• Telethon

⚡ Fast • Safe • Secure

Tap the button below to begin 👇
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


# 🔄 RECHECK SUBSCRIPTION
@app.on_callback_query(filters.regex("check_sub"))
async def check_sub(client, callback):
    is_joined = await force_subscribe(client, callback.message)

    if not is_joined:
        await callback.answer("❌ You must join the channel first!", show_alert=True)
        return

    await callback.message.delete()
    await start(client, callback.message)


# ⚙️ GENERATE SESSION MENU
@app.on_callback_query(filters.regex("generate"))
async def generate_menu(client, callback):
    await callback.message.reply(
        """
━━━━━━━━━━━━━━━━━━
🔐 GENERATE STRING SESSION
━━━━━━━━━━━━━━━━━━

Before generating a session,
make sure you have:

• Telegram API ID
• Telegram API HASH

Choose an option below 👇
━━━━━━━━━━━━━━━━━━
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔑 Create API ID & HASH",
                        url="https://my.telegram.org/auth"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🐍 Pyrogram Session",
                        url="https://telegram.tools/session-string-generator#pyrogram,user"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📡 Telethon Session",
                        url="https://telegram.tools/session-string-generator#telethon,user"
                    )
                ]
            ]
        )
    )
    await callback.answer()


app.run()
