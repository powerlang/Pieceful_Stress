import json
import random


def rarelyHappen():
    return random.choice([True, False, False, False])


def maybeHappen():
    return random.choice([True, False])


def randomChar():
    head = random.randint(0xB0, 0xCF)
    body = random.randint(0xA, 0xF)
    tail = random.randint(0, 0xF)

    val = ( head << 8 ) | (body << 4) | tail
    str = "%x" % val

    return bytes.fromhex(str).decode('gb2312')


def randomWord(length=2):
    try:
        return "".join([randomChar() for i in range(length)])
    except:
        return "东京"


def getResData(res, key):
    try:
        data = json.loads(res.text)["result"][key]
    except:
        data = None

    return data


def isAnonymous(session):
    return "Authorization" not in session.headers
