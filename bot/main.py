#!./bin/python
from os import environ, path
from sys import argv
from pyrogram import Client, MessageHandler
import yaml

conf = yaml.load(open('%s/conf.yml' %
                      path.dirname(path.abspath(__file__)), 'r'), Loader=yaml.SafeLoader)
if not conf.get('tgresender', False):
    print('No Valid Config Provided')

conf = conf['tgresender']

if not conf.get('api_id', False) or not conf.get('api_hash', False):
    print('No API_ID or API_HASH provided')

api_id, api_hash = conf['api_id'], conf['api_hash']

app = Client(
    "tgresender",
    api_id=api_id,
    api_hash=api_hash,
    workdir=environ.get('WORKDIR', '%s/../shared/' %
                        path.dirname(path.abspath(__file__)))
)

resend_from = conf['resend'].keys()


@app.on_message()
def resend(client, message):
    global argv
    if "--verbose" in argv:
        print(
            "Got message from: {} - {}".format(message.chat.username or
                                               message.chat.title, message.chat.username or message.chat.id)
        )
    try:
        def forward_messages(chat_id, from_chat_id, message_ids, as_copy):
            client.forward_messages(
                chat_id=chat_id, from_chat_id=from_chat_id, message_ids=message_ids, as_copy=as_copy)

        if message.chat.username in resend_from:
            resend_to = conf['resend'][message.chat.username]['to']
            as_copy = conf['resend'][message.chat.username]['copy']
        elif str(message.chat.id) in resend_from:
            resend_to = conf['resend'][str(message.chat.id)]['to']
            as_copy = conf['resend'][str(message.chat.id)]['copy']
        else:
            return

        forward_messages(chat_id=resend_to, from_chat_id=message.chat.id,
                         message_ids=message.message_id, as_copy=as_copy)
    except:
        pass


try:
    app.start()
except ConnectionError:
    app.disconnect()
    app.start()
