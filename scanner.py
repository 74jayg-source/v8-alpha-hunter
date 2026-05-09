import os
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

print("Token exists:", bool(BOT_TOKEN))
print("Chat ID exists:", bool(CHAT_ID))

message = "🚀 V8 Alpha Hunter test message"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    json={
        "chat_id": CHAT_ID,
        "text": message
    },
    timeout=20
)

print("Telegram status:", response.status_code)
print("Telegram response:", response.text)

response.raise_for_status()
