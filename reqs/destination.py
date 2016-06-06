import utils


def getDestination(session, destId):
    r = session.get("/destination/{}/".format(destId), name="/destination/[id]")
    return utils.getResData(r, "destination")


def getCountries(session, destId):
    r = session.get("/destination/{}/countries/".format(destId), name="/destination/[id]/countries")
    return utils.getResData(r)


def destinationCards(session, destId, q="", tag=0, order=1, last="", start=0, count=24):
    r = session.get("/destination/{}/cards/?q={}&tag={}&order={}&last={}&start={}&count={}".format(destId, q, tag, order, last, start, count),
                    name="/destination/[id]/cards")
    return utils.getResData(r)


def destinationMajorCountries(session, last="", start=0, count=24):
    r = session.get("/destination/major-countries/?last={}&start={}&count={}".format(last, start, count), name="/destination/major-countries")
    return utils.getResData(r)


def destinationFeaturedCards(session, destId, last="", start=0, count=24):
    r = session.get("/destination/{}/featured-cards/?last={}&start={}&count={}".format(destId, last, start, count), name="/destination/[id]/featured-cards")
    return utils.getResData(r)


def destinationPopularCities(session, destId):
    r = session.get("/destination/{}/popular-cities".format(destId), name="/destination/[id]/popular-cities")
    return utils.getResData(r)


def destinationPopularPois(session, destId, last="", start=0, count=24):
    r = session.get("/destination/{}/popular-pois/?last={}&start={}&count={}".format(destId, last, start, count), name="/destination/[id]/featured-pois")
    return utils.getResData(r)


def destinationRecommend(session, destId):
    r = session.get("/destination/{}/recommend/".format(destId), name="/destination/[id]/recommend")
    return utils.getResData(r, "destinations")


def destinationPopularTrips(session, destId):
    r = session.get("/destination/{}/popular-trips/".format(destId), name="/destination/[id]/featured-trips")
    return utils.getResData(r, "trips")


def destinationPopularBoxes(session, destId):
    r = session.get("/destination/{}/popular-boxes/".format(destId), name="/destination/[id]/featured-boxes")
    return utils.getResData(r, "boxes")


def destinationClip(session, destId):
    r = session.put("/destination/{}/clip/".format(destId), name="/destination/[id]/clip")
    return utils.getResData(r)


def destinationUnclip(session, destId):
    r = session.put("/destination/{}/unclip/".format(destId), name="/destination/[id]/unclip")
    return utils.getResData(r)


def destinationIsCliped(session, destId):
    r = session.get("/destination/{}/clip/".format(destId), name="/destination/[id]/clip")
    return utils.getResData(r, "clipped")
