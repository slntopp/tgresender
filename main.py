from os import environ
from pyrogram import Client
from dotenv import load_dotenv

load_dotenv()

app = Client(
    "tgresender",
    api_id=environ['API_ID'],
    api_hash=environ['API_HASH']
)
app.run()
