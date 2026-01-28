from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)
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


# ================= FORCE SUB CHECK =================
async def is_subscribed(client, user_id):
    try:
        await client.get_chat_member(FORCE_SUB_CHANNEL, user_id)
        return True
    except UserNotParticipant:
        return False
    except Exception:
        return False


# ================= START =================
@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    if not await is_subscribed(client, message.from_user.id):
        # 🔑 username -> valid https url
        join_link = f"https://t.me/{FORCE_SUB_CHANNEL.lstrip('@')}"

        await message.reply(
            "🔒 **Join our channel to use this bot**\n\nAfter joining, click **Try Again** 👇",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("📢 Join Channel", url=join_link)],
                    [InlineKeyboardButton("🔄 Try Again", callback_data="recheck")]
                ]
            )
        )
        return

    await message.reply(
        f"""
━━━━━━━━━━━━━━━━━━━━━━
𖤐 𝗦𝗧𝗗 𝗦𝗧𝗥𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 𝗕𝗢𝗧 𖤐
━━━━━━━━━━━━━━━━━━━━━━

👋 𝗛𝗲𝘆, **{message.from_user.first_name}**

⚡ 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗦𝘁𝗿𝗶𝗻𝗴 𝗦𝗲𝘀𝘀𝗶𝗼𝗻𝘀 𝗶𝗻 𝗼𝗻𝗲 𝗰𝗹𝗶𝗰𝗸 🚀

━━━━━━━━━━━━━━━━━━━━━━
✨ 𝗦𝘂𝗽𝗽𝗼𝗿𝘁𝗲𝗱
━━━━━━━━━━━━━━━━━━━━━━
🔑 𝗔𝗣𝗜 𝗜𝗗 & 𝗔𝗣𝗜 𝗛𝗔𝗦𝗛  
🐍 𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺  
📡 𝗧𝗲𝗹𝗲𝘁𝗵𝗼𝗻  

━━━━━━━━━━━━━━━━━━━━━━
⚡ 𝗙𝗮𝘀𝘁 • 𝗦𝗮𝗳𝗲 • 𝗦𝗲𝗰𝘂𝗿𝗲
━━━━━━━━━━━━━━━━━━━━━━
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⚙️ 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝗦𝗲𝘀𝘀𝗶𝗼𝗻", callback_data="generate")],
                [
                    InlineKeyboardButton("📢 𝗖𝗵𝗮𝗻𝗻𝗲𝗹", url=CHANNEL_LINK),
                    InlineKeyboardButton("🆘 𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url=SUPPORT_LINK)
                ]
            ]
        )
    )


# ================= RECHECK =================
@app.on_callback_query(filters.regex("^recheck$"))
async def recheck(client, callback):
    if not await is_subscribed(client, callback.from_user.id):
        await callback.answer("❌ Please join the channel first!", show_alert=True)
        return

    await callback.message.delete()
    await start(client, callback.message)


# ================= GENERATE MENU =================
@app.on_callback_query(filters.regex("^generate$"))
async def generate(client, callback):
    await callback.message.reply(
        """
━━━━━━━━━━━━━━━━━━
🔐 **GENERATE STRING SESSION**
━━━━━━━━━━━━━━━━━━

You will need:
• Telegram API ID
• Telegram API HASH

Choose an option 👇
━━━━━━━━━━━━━━━━━━
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔑 Create API ID & HASH",
                        web_app=WebAppInfo(url="https://my.telegram.org/auth")
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🐍 Pyrogram Session",
                        web_app=WebAppInfo(
                            url="https://telegram.tools/session-string-generator#pyrogram,user"
                        )
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📡 Telethon Session",
                        web_app=WebAppInfo(
                            url="https://telegram.tools/session-string-generator#telethon,user"
                        )
                    )
                ]
            ]
        )
    )
    await callback.answer()


app.run()
