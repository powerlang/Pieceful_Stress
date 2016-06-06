import utils


def authLogin(session, email, password):
    r = session.post("/auth/login/", {"email": email, "password": password})
    return utils.getResData(r, "token")


def authRegister(session, email, password):
    r = session.post("/auth/register/", {"email": email, "password": password})
    return utils.getResData(r, "token")


def authRefreshStatus(session):
    r = session.get("/auth/refresh-status/")
    return utils.getResData(r, "account")


def userFollowed(session, userId):
    r = session.get("/user/{}/followed/".format(userId), name="/user/[id]/followed")
    return utils.getResData(r, "followed")


def followUser(session, userId):
    session.post("/user/follow-user/", {"targetUser": userId})
    return True


def userBoxes(session, userId, q="", order=1, last="", start=0, count=24):
    r = session.get("/user/{}/boxes/?q={}&order={}&last={}&start={}&count={}".format(userId, q, order, last, start, count),
                    name="/user/[id]/boxes")
    return utils.getResData(r, ["boxes", "hasMore"])


def userCards(session, userId, q="", tag=0, order=1, last="", start=0, count=24):
    r = session.get("/user/{}/cards/?q={}&tag={}&order={}&last={}&start={}&count={}".format(userId, q, tag, order, last, start, count),
                    name="/user/[id]/cards")
    return utils.getResData(r, ["cards", "hasMore"])


def userBackpacks(session, userId):
    r = session.get("/user/{}/backpacks/".format(userId), name="/user/[id]/backpacks")
    return utils.getResData(r, "backpacks")


def userInfo(session, userId):
    r = session.get("/user/{}/".format(userId), name="/user/[id]")
    return utils.getResData(r, "user")
