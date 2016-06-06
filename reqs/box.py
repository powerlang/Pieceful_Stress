import utils


def newBox(session, boxData):
    boxData.setdefault("title", "压力测试盒子")
    r = session.post("/box/new/", boxData)
    return utils.getResData(r, "box")


def boxInfo(session, boxId):
    r = session.get("/box/{}".format(boxId), name="/box/[id]")
    return utils.getResData(r, "box")


def boxCards(session, boxId, q="", tag=0, order=1, last="", start=0, count=24):
    r = session.get("/box/{}/cards/?q={}&tag={}&order={}&last={}&start={}&count={}".format(boxId, q, tag, order, last, start, count),
                    name="/box/[id]/cards")
    return utils.getResData(r, ["cards", "hasMore"])
