import json
import random
import redis
import settings


def rarelyHappen():
    return random.choice([True, False, False, False])


def maybeHappen():
    return random.choice([True, False])


def randomChar():
    head = random.randint(0xB0, 0xCF)
    body = random.randint(0xA, 0xF)
    tail = random.randint(0, 0xF)

    val = (head << 8) | (body << 4) | tail
    str = "%x" % val

    return bytes.fromhex(str).decode('gb2312')


def weightedChoice(choices):
    if isinstance(choices, dict):
        choices = list(choices.items())

    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w >= r:
            return c
        upto += w


def statWeight(weights, records):
    for record in records:
        weights.setdefault(record, 0)
        weights[record] += 1


def ajustWeight(weights, record):
    weights[record] = 1


def randomWord(length=2):
    try:
        return "".join([randomChar() for i in range(length)])
    except:
        return "东京"


def getResData(res, key=None):
    try:
        result = json.loads(res.text)["result"]
    except:
        return None

    if key is None:
        return result

    if not isinstance(key, list):
        return result.get(key)

    return {k: result.get(k) for k in key}


def isAnonymous(session):
    return "Authorization" not in session.headers


redisPool = redis.ConnectionPool.from_url(settings.REDIS)
def getRedisClient():
    return redis.Redis(connection_pool=redisPool)


def clearUsers(module):
    getRedisClient().set("{}-fake-users".format(module), 0)


def getNextUser(module):
    userIndex = getRedisClient().incr("{}-fake-users".format(module))
    return {"email": settings.FAKE_EMAIL_FORMAT.format(index=userIndex),
            "password": "123456"}
