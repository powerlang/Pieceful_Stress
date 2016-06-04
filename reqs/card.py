import json
import utils


def getCard(session, cardId):
    r = session.get("/card/{}/".format(cardId), name="/card/[id]")
    return utils.getResData(r, "card")


def getCardComments(session, cardId):
    r = session.get("/card/{}/comments/".format(cardId), name="/card/[id]/comments")
    return utils.getResData(r, "comments")


def getRelatedCards(session, cardId):
    r = session.get("/card/{}/related-cards/".format(cardId), name="/card/[id]/related-cards")
    return utils.getResData(r, "cards")


def getRelatedBoxes(session, cardId):
    r = session.get("/card/{}/related-boxes/".format(cardId), name="/card/[id]/related-boxes")
    return utils.getResData(r, "boxes")


def likeCard(session, cardId):
    r = session.post("/card/{}/like/".format(cardId), name="/card/[id]/like")
    return utils.getResData(r, "liked")


def clipCard(session, cardId, boxId):
    session.put("/card/{}/clip/".format(cardId), {"box": boxId}, name="/card/[id]/clip/")
    return True


def newCard(session, cardData):
    cardData.setdefault("title", "压力测试笔记")
    cardData.setdefault("type", 0)
    cardData.setdefault("content", json.dumps([{"tag": "p", "contents": ["\u5bf9\u4e8e\u4e00\u4e2a\u5728\u4e1c\u4eac\u751f\u6d3b\u8fc7\u4e09\u5e74\u96f6\u4e09\u4e2a\u6708\u7684\u4eba\u6765\u8bf4\uff0c\u5047\u5982\u7ed9\u6211\u4e09\u65e5\u4e1c\u4eac\u6211\u60f3\u6211\u4f1a\u5728\u8fd9\u91cc\u8fd9\u6837\u751f\u6d3b\u3002"]}, {"tag": "p", "contents": ["DAY1"]}, {"tag": "p", "contents": ["\u8fea\u65af\u5c3c\u4e50\u56ed"]}, {"tag": "p", "contents": ["DAY2"]}, {"tag": "p", "contents": ["\u5409\u7965\u5bfa"]}, {"tag": "p", "contents": ["DAY3"]}, {"tag": "p", "contents": ["\u539f\u5bbf\u660e\u6cbb\u795e\u5bab"]}, {"tag": "p", "contents": ["\u4e1c\u4eac\u5854"]}]))

    r = session.post("/card/new/", cardData)
    return utils.getResData(r, "card")
