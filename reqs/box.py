import utils


def newBox(session, boxData):
    boxData.setdefault("title", "压力测试盒子")
    r = session.post("/box/new/", boxData)
    return utils.getResData(r, "box")
