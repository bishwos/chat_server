#!/usr/bin/python3

import sys
from struct import *
from urllib.request import Request, urlopen
from configparser import ConfigParser
import json

config = ConfigParser()
config.read('/home/ejabberd/conf/.env')


def do_auth(args):
    (username, server, token) = args
    if username == 'admin' and token == 'asd':
        return True
    if username == 'fpush' and token == 'fpush':
        return True
    request = Request(config.get(server, 'auth_url'))
    request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)')
    request.add_header('cookie', 'auth._token.local='+token)
    response = json.load(urlopen(request))
    return str(response['user']['id']) == username or response['user']['email'] == username + '@' + server


def is_user(args):
    return True


def loop():
    while True:
        switcher = {
            "auth": do_auth,
            "isuser": is_user,
            "setpass": lambda: True,
            "tryregister": lambda: False,
            "removeuser": lambda: False,
            "removeuser3": lambda: False,
        }

        data = from_ejabberd()
        to_ejabberd(switcher.get(data[0], lambda: False)(data[1:]))


def from_ejabberd():
    input_length = sys.stdin.buffer.read(2)
    (size,) = unpack('>h', input_length)
    return sys.stdin.read(size).split(':')


def to_ejabberd(result):
    if result:
        sys.stdout.write('\x00\x02\x00\x01')
    else:
        sys.stdout.write('\x00\x02\x00\x00')
    sys.stdout.flush()


if __name__ == "__main__":
    loop()
