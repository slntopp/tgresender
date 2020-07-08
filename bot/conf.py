import yaml
from sys import argv
from os import path


def set_api(api_id, api_hash):
    conf = load()
    conf['api_id'] = api_id
    conf['api_hash'] = api_hash
    yaml.dump(
        {'tgresender': conf}, open('%s/conf.yml' %
                                   path.dirname(path.abspath(__file__)), 'w')
    )
    return True


def set_resender(rules: dict):
    conf = load()
    conf['rules'] = rules
    yaml.dump(
        {'tgresender': conf}, open('%s/conf.yml' %
                                   path.dirname(path.abspath(__file__)), 'w')
    )
    return True


def load() -> dict:
    """Loades config from bot/conf.yml

    Returns:
        dict: Configuration
    """
    conf = yaml.load(open('%s/conf.yml' %
                          path.dirname(path.abspath(__file__)), 'r'), Loader=yaml.SafeLoader)
    if not conf.get('tgresender', False):
        print('No Valid Config Provided')

    conf = conf['tgresender']
    if not conf.get('api_id', False) or not conf.get('api_hash', False):
        print('No API_ID or API_HASH provided')
    return conf


if __name__ == "__main__":
    print('Configuration:')
    try:
        import json
        r = json.dumps(load(), sort_keys=False, indent=4)
        print(r)
    except Exception as e:
        print('Failed: ', e)
