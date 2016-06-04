import utils


def searchPlaces(session, q, tag):
    r = session.get("/search/place/?q={}&tag={}".format(q, tag), name="/search/place")
    return utils.getResData(r, "places")
