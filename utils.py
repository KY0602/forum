import scrypt, base64, configparser, random, json
import re
from datetime import datetime, timedelta
from .models import *
import random, string, jwt


def encrypt_password(pw):
    config = configparser.RawConfigParser()
    config.read('config.cfg')
    db_dict = dict(config.items('DATABASE'))
    salt = db_dict["salt"]
    key = scrypt.hash(pw, salt, 32768, 8, 1, 32)
    return base64.b64encode(key).decode("ascii")


def checkregister(content):
    # Password (Length between 6-10)
    if len(content['username'])<6 or len(content['username'])>10:
        return "username", False

    # Password (Length between 6-18, containing lower-case, upper-case and numbers)
    if re.match("^(?![0-9]+$)(?![A-Z]+$)(?![a-z]+$)(?![a-zA-Z]+$)(?![0-9A-Z]+$)(?![0-9a-z]+$)[0-9A-Za-z]{6,18}$",content['password'])==None:
        return "password", False

    # Email
    if re.match(
            "[a-zA-Z0-9]{1,63}@(([a-zA-Z0-9]+[a-zA-Z0-9-]*[a-zA-Z0-9]+\.)|([a-zA-Z0-9]*\.)|(\.))*(([a-zA-Z]+[a-zA-Z-]*[a-zA-Z]+)|([a-zA-Z]+)|([a-zA-Z0-9]+([a-zA-Z0-9-]*[a-zA-Z-]+[a-zA-Z0-9-]*)+[a-zA-Z0-9]+)|())$",
            content['email']) == None:
        return "email", False

    place = int((content['email']).find('@'))
    if len(content['email']) - place > 63:
        return "email", False

    return "ok", True



