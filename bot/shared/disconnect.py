import conf
from pyrogram import Client


def disconnect(client: Client):
    print('Disconnecting...')
    app.disconnect()
    print('Disconnected succesful!')


if __name__ == '__main__':
    conf = conf.load()
    api_id, api_hash = conf['api_id'], conf['api_hash']
    app = gen_client(api_id, api_hash)
    disconnect(app)
