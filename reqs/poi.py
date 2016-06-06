import utils


def getPoi(session, poiId):
    r = session.get("/poi/{}/".format(poiId), name="/poi/[id]")
    return utils.getResData(r, "poi")


def poiCards(session, poiId, last="", start=0, count=24):
    r = session.get("/poi/{}/cards/?last={}&start={}&count={}".format(poiId, last, start, count), name="/poi/[id]/cards")
    return utils.getResData(r)


def poiPhotos(session, poiId, last="", start=0, count=24):
    r = session.get("/poi/{}/photos/?last={}&start={}&count={}".format(poiId, last, start, count), name="/poi/[id]/photos")
    return utils.getResData(r)


def poiRecommendPois(session, poiId):
    r = session.get("/poi/{}/recommend-pois/".format(poiId), name="/poi/[id]/recommend-pois")
    return utils.getResData(r, "pois")


def poiClip(session, poiId):
    r = session.put("/poi/{}/clip/".format(poiId), name="/poi/[id]/clip")
    return utils.getResData(r)


def poiUnclip(session, poiId):
    r = session.put("/poi/{}/unclip/".format(poiId), name="/poi/[id]/unclip")
    return utils.getResData(r)


def poiIsCliped(session, poiId):
    r = session.get("/poi/{}/clip/".format(poiId), name="/poi/[id]/clip")
    return utils.getResData(r, "clipped")
