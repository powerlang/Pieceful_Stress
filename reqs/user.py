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


def userBoxes(session, userId):
    r = session.get("/user/{}/boxes/".format(userId), name="/user/[id]/boxes")
    return utils.getResData(r, "boxes")
