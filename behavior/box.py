import utils
from reqs import BoxReqs


def boxHome(session, boxId):
    BoxReqs.boxInfo(session, boxId)

    cardIds, hasMore = [], False
    data = BoxReqs.boxCards(session, boxId)
    if data:
        cardIds = [card["id"] for card in data["cards"]]
        hasMore = data["hasMore"]

    while hasMore and utils.maybeHappen():
        data = BoxReqs.boxCards(session, boxId, last=cardIds[-1])
        if data:
            cardIds.extend([card["id"] for card in data["cards"]])
            hasMore = data["hasMore"]
        else:
            hasMore = False

    return {"cards": cardIds}
