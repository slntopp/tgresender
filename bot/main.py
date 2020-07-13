#!./bin/python
from os import environ, path, listdir
from sys import argv
from pyrogram import Client, MessageHandler
import yaml
import re

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
    workdir='/shared'
)

def log_in_file(msg):
    l = open('/shared/msg.log', 'a')
    l.write(msg + '\n')
    l.close()

def log(msg):
  print(msg)
  log_in_file(msg)
    
resend_from = conf['resend'].keys()
if "--verbose" in argv:
  msg = "Watching for: %s" % resend_from
  log(msg)


@app.on_message()
def resend(client, message):
    global argv
    try:
        if "--verbose" in argv:
            msg = "Got message from: {} - {}".format(message.chat.username or
                                               message.chat.title, message.chat.username or message.chat.id)
            log(msg)
        def forward_messages(chat_id, from_chat_id, message_ids, as_copy):
            client.forward_messages(
                chat_id=chat_id, from_chat_id=from_chat_id, message_ids=message_ids, as_copy=as_copy)

        if "--verbose" in argv:
            msg = 'Seeking for "%s" and "%s" in %s' % (message.chat.username, str(message.chat.id), resend_from)
            msg += '\nResult username: %s' % str(message.chat.username in resend_from)
            msg += '\nResult chat id: %s' % str(str(message.chat.id) in resend_from)
            log(msg)
        if message.chat.username in resend_from:
            resend_to = conf['resend'][message.chat.username]['to']
            as_copy = conf['resend'][message.chat.username]['copy']
        elif str(message.chat.id) in resend_from:
            log_in_file(str(conf['resend']))
            resend_to = conf['resend'][str(message.chat.id)]['to']
            as_copy = conf['resend'][str(message.chat.id)]['copy']
        else:
            return

        resend_to = int(resend_to) if resend_to[0] == '-' else resend_to
        forward_messages(chat_id=resend_to, from_chat_id=message.chat.id,
                         message_ids=message.message_id, as_copy=as_copy)
    except Exception as e:
        log('Exception catched: %s' % e)

import sqlite3

try:
    app.start()
except sqlite3.OperationalError as e:
    log(e.__dict__)
except ConnectionError:
    app.disconnect()
    app.start()
