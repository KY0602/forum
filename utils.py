import scrypt, base64, configparser, random, json
import re
from datetime import datetime, timedelta
from .models import *
from fuzzywuzzy import process
import random, string, jwt


def encrypt_password(pw):
    config = configparser.RawConfigParser()
    config.read('config.cfg')
    db_dict = dict(config.items('DATABASE'))
    salt = db_dict["salt"]
    key = scrypt.hash(pw, salt, 32768, 8, 1, 32)
    return base64.b64encode(key).decode("ascii")


def check_username(username):
    return (len(username) >= 6) and (len(username) <= 10)


def check_password(password):
    if (re.match("^(?![0-9]+$)(?![A-Z]+$)(?![a-z]+$)(?![a-zA-Z]+$)(?![0-9A-Z]+$)(?![0-9a-z]+$)[0-9A-Za-z]{6,18}$",
                 password) is None):
        return False
    else:
        return True


def check_len255(text):
    return (len(text) >= 0) and (len(text) <= 255)


def checkregister(content):
    # Username (Length between 6-10)
    if not check_username(content['username']):
        return "username", False

    # Password (Length between 6-18, containing lower-case, upper-case and numbers)
    if not check_password(content['password']):
        return "password", False

    # Email
    if re.match(
            "[a-zA-Z0-9]{1,63}@(([a-zA-Z0-9]+[a-zA-Z0-9-]*[a-zA-Z0-9]+\.)|([a-zA-Z0-9]*\.)|(\.))*(([a-zA-Z]+[a-zA-Z-]*[a-zA-Z]+)|([a-zA-Z]+)|([a-zA-Z0-9]+([a-zA-Z0-9-]*[a-zA-Z-]+[a-zA-Z0-9-]*)+[a-zA-Z0-9]+)|())$",
            content['email']) is None:
        return "email", False

    place = int((content['email']).find('@'))
    if len(content['email']) - place > 63:
        return "email", False

    return "ok", True


def check_valid(username, password, description):
    # Username (Length between 6-10)
    if not check_username(username):
        return "username", False

    # Password (Length between 6-18, containing lower-case, upper-case and numbers)
    if not check_password(password):
        return "password", False

    # Description (Length between 0-255):
    if not check_len255(description):
        return "description", False

    return "ok", True


def fuzzysearch(key, options, threshold=75):
    ratios = process.extract(key, options)
    selected = []
    for i in ratios:
        if i[1] > threshold:
            selected.append(i[0])
    return selected
