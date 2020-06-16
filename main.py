#!./bin/python
from os import environ
from pyrogram import Client, MessageHandler
from dotenv import load_dotenv

load_dotenv()

resend_from, resend_to = environ['RESEND_FROM'], environ['RESEND_TO']

app = Client(
    "TgResender",
    api_id=environ['API_ID'],
    api_hash=environ['API_HASH']
)

@app.on_message()
def resend(client, message):
    try:
        if message.from_user.is_bot: return
        if resend_from in (message.from_user.username, message.from_user.id):
            client.forward_messages(chat_id=resend_to, from_chat_id=message.chat.id, message_ids=message.message_id)
    except:
        pass

try:
    app.start()
except ConnectionError:
    app.disconnect()
    app.start()