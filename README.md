# StringSessionGen

An advanced Telegram string session generator bot with a modern web-based interface and force subscribe support.

This bot allows users to generate Telegram string sessions easily for popular client libraries using a clean and simple flow directly from Telegram.

---

## 🚀 Features

- 🔐 Force subscribe protection
- 🌐 Modern web-based session generation
- ⚡ Fast and lightweight
- 🤖 Clean Telegram bot UI
- 🔑 API ID & API HASH helper
- 🧩 Supports multiple client libraries

---

## 📦 Supported Clients

- Pyrogram
- Telethon

---

## 🛠 How It Works

1. User starts the bot
2. Bot checks force subscription
3. User joins the required channel
4. User selects **Generate Session**
5. Web interface opens directly inside Telegram
6. User generates and copies their session string

---

## ⚠️ Security Notice

- This bot **does not store** any session strings
- All session generation happens on external web pages
- Never share your session string with anyone
- Anyone with your session string can access your account

---

## 🧪 Requirements

- Python 3.10+
- Pyrogram
- tgcrypto

---

## ⚙️ Deployment

This bot is ready to deploy on platforms like:

- Heroku   https://heroku.com/deploy?template=https://github.com/StdBots/StringSessionGen

- VPS / Dedicated server
- Any Python-supported hosting

Make sure to set the required environment variables before running the bot.

---

## 📄 Environment Variables
 API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
FORCE_SUB_CHANNEL=@your_channel
CHANNEL_LINK=https://t.me/your_channel

SUPPORT_LINK=https://t.me/your_support


---

## 📌 Status

This project is actively maintained.  
More improvements and features will be added over time.

---

## 📜 License

Apache License 2.0  
You are free to use, modify, and distribute this project with proper attribution.

---

## ⭐ Credits

Developed as part of the **StdBots** ecosystem.



