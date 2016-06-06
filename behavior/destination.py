import utils
from reqs import DestinationReqs


def destinationDetial(session, destId):
    DestinationReqs.getDestination(session, destId)

    result = {"cards": [], "users": [], "boxes": []}

    cardIds, userIds, boxIds, hasMore = [], [], [], False
    data = DestinationReqs.destinationCards(session, destId)
    if data:
        cardIds = [card["id"] for card in data["cards"]]
        userIds = [card["owner"]["id"] for card in data["cards"]]
        boxIds = [card["box"]["id"] for card in data["cards"] if card.get("box")]
        hasMore = data["hasMore"]

    while hasMore and utils.maybeHappen():
        data = DestinationReqs.destinationCards(session, destId, last=cardIds[-1])
        if data:
            cardIds.extend([card["id"] for card in data["cards"]])
            userIds.extend([card["owner"]["id"] for card in data["cards"]])
            boxIds.extend([card["box"]["id"] for card in data["cards"] if card.get("box")])
            hasMore = data["hasMore"]
        else:
            hasMore = False

    result["cards"] = cardIds
    result["users"] = userIds
    result["boxes"] = boxIds

    return result
