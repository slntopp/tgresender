import conf
from server import tg_app
from pyrogram import MessageHandler

conf = conf.load()
app = tg_app["app"]


@ app.on_message()
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
