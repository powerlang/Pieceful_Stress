import utils


def exploreCards(session, page):
    r = session.get("/explore/?start={}".format(24*page), name="/explore")
    return utils.getResData(r, "cards")
