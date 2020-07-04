import conf
from generate_session import gen_client

if __name__ == '__main__':
    conf = conf.load()
    api_id, api_hash = conf['api_id'], conf['api_hash']
    app = gen_client(api_id, api_hash)
    app.connect()
    chats = []
    for d in app.iter_dialogs():
        chats.append({
            "title": d.chat.first_name or d.chat.title or 'NO TITLE',
            "id": d.chat.username or d.chat.id or 'NOTHING'
        })
    for ch in sorted(chats, key=lambda k: k['title']):
        print("{title} -> {id}".format(**ch))
    app.disconnect()
