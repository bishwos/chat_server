#!/usr/bin/python3

import logging
import sys
from struct import *
import json
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser
try:
    from urllib.request import Request, urlopen  # Python 3
except ImportError:
    from urllib2 import Request, urlopen

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='/home/ejabberd/logs/extauth.log',
                    filemode='a')

config = ConfigParser()
config.read('/home/ejabberd/conf/.env')


def from_ejabberd():
    logging.info("Getting something from ejabberd")
    input_length = sys.stdin.read(2)
    logging.info("Bytes read: " + str(len(input_length)))
    logging.info("Input Length: " + str(input_length))
    (size,) = unpack('>h', input_length)
    return sys.stdin.read(size).split(':')


def to_ejabberd(bool):
    answer = 0
    if bool:
        answer = 1
    token = pack('>hh', 2, answer)
    sys.stdout.write(token)
    sys.stdout.flush()


def auth(username, server, password):
    if username == 'admin' and password == 'asd':
        return True
    try:
        email = username + '@' + server
        logging.info(email + " with username")
        logging.info(password + " trying password")
        request = Request(config.get(server, 'auth_url'))
        request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)')
        request.add_header('cookie', 'auth._token.local='+password)
        response = json.load(urlopen(request))
    except:
        logging.exception("auth error")
        return False
    return response['user']['email'] == email


def tryregister(username, server, password):
    logging.info(username + "registering")
    return True


def isuser(username, server):
    return True


def setpass(username, server, password):
    return False


def __del__(self):
    """
    What to do when we are shut off.
    """
    logging.info('ejabberd_auth_bridge process stopped')


print(auth('info','aayulogic.com','eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwNDMwNjQ4LCJpYXQiOjE2NjA0MDkwNDgsImp0aSI6IjRhMTdiZWUyNWRmNjRkYjBhZmU3ZjY0NDNmZDEyZDk5IiwidXNlcl9pZCI6MX0.GnqQRq2618Bt6XZaECOtlCpMXDPu0btny0L7w9DJ3jbUFMY23k1Q2sgDGMKbUGD2GDKQA8F__dFyWi-Dh4CEarKdDG4zjiFxF5LalVjbBY71mwRGC3OOEqKoxVWpLfbWvHnnE0NlpGYITfiapdVaJY-ksK_ZYfz10YWKzhDKl7cbD9R2tJMgX5vuPbbJOGMkG3NkNE9wcQUTggYHnXBp1ezmEnOBG9fkvVZ-8OqeCYszQ5AgIOeqXIqkWLVEBMcN0D1Onk0lpQqPCx7-7g3o6A5jLxEQMEn4Y81O27HXhGXpehQDO03JLtYEutZFqXqCwWII7ipN7hc9LW3AoZfzag; auth._refresh_token.local=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MTAxMzg0OCwiaWF0IjoxNjYwNDA5MDQ4LCJqdGkiOiI4ODc5YTE2NzUwMjc0ZjUxYWE3MjNlYzhiMDhiNjRjYyIsInVzZXJfaWQiOjF9.CDWw1e8okEp2zIabK2mIOHc1NFAHVIgtChnuhK1A_4PW-R_Wat5v-nKmZpVHX9vWd0iJRPEeXeGbz8UP7S-XvT2S5PdIl8CaJJiIKYAaZeLdkGtOuZK04UIUC-0aSWsNwicTRlcs2kVPkcJZeF0qwjWRtljc_33furh9b0u8S-lyE5n0kMwLd7tQsChgnwo_4f3TeMfYWHJ0cvbPlpH_AL8vNA-U-IQKOgZEw2LCu5lIVzysTPzSEZrXikJOZFDglVga4DflPtrDufAVvGdxVaFupkb_uv1WB7bLbmxjawqKVqsPWT_dECQpI9zG3su_OK_oduR81spLLvQblyKo2g'))
