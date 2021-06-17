#####################################################################
# You can ignore this script, it will be needed just to be able     #
# to go through this process without CLI                            #
#####################################################################
import conf
from os import environ, listdir, path
from getpass import getpass
from pyrogram import Client, errors


def gen_client(api_id: str, api_hash: str) -> Client:
    """Generates Client instance, nothing special

    Args:
        api_id (str): Telegram App API ID
        api_hash (str): Telegram App API Hash key

    Returns:
        Pyrogram::Client
    """
    return Client(
        "tgresender",
        api_id=api_id,
        api_hash=api_hash
    )


def send_code(app: Client, phone: str):
    print("Sending code...")
    try:
        r = app.send_code(phone)
    except errors.BadRequest:
        print("Send code failed")
    print("Code sent...")
    phone_code_hash = r.phone_code_hash
    return phone_code_hash


def enter_code(app: Client, phone: str, phone_code_hash: str, code: str):
    try:
        user = app.sign_in(phone, phone_code_hash, code)
        return user
    except errors.SessionPasswordNeeded:
        return False


if __name__ == '__main__':
    conf = conf.load()
    api_id, api_hash = conf['api_id'], conf['api_hash']
    app = gen_client(api_id, api_hash)

    print("Connecting to Telegram Servers...")
    try:
        r = app.connect()
        if not r:
            print("Unexpected connection error")
    except ConnectionError:
        print("Client was already connected, disconnect first")
        exit(1)

    phone = input("Enter your phone number with country code: ")
    phone_code_hash = send_code(app, phone)

    code = input("Enter the confirmation code: ")
    r = enter_code(app, phone, phone_code_hash, code)
    if r:
        user = r
    else:
        print("Password is required")
        print("Your hint: %s" % app.get_password_hint())
        passwd = getpass("Enter your password: ")
        user = app.check_password(passwd)

    if not user.is_bot:
        print('Welcome, {}'.format(user.first_name))

    for i in range(3):
        print()

    print('Your session file stored at %s' %
          '/'.join(path.dirname(path.abspath(__file__)).split('/')[:-1] + ['tgresender.session']))
