import utils
from reqs import PoiReqs


def poiDetail(session, poiId):
    PoiReqs.getPoi(session, poiId)

    result = {"cards": [], "pois": []}

    cardIds, hasMore = [], False
    data = PoiReqs.poiCards(session, poiId)
    if data:
        cardIds = [card["id"] for card in data["cards"]]
        hasMore = data["hasMore"]

    while hasMore and utils.maybeHappen():
        data = PoiReqs.poiCards(session, poiId, last=cardIds[-1])
        if data:
            cardIds.extend([card["id"] for card in data["cards"]])
            hasMore = data["hasMore"]
        else:
            hasMore = False

    result["cards"] = cardIds

    pois = PoiReqs.poiRecommendPois(session, poiId)
    if pois:
        result["pois"] = [poi["id"] for poi in pois]

    return result
