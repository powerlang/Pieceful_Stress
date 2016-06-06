import utils
from reqs import UserReqs


def userHome(session, userId):
    UserReqs.userInfo(session, userId)

    cardIds, hasMore = [], False
    data = UserReqs.userCards(session, userId)
    if data:
        cardIds = [card["id"] for card in data["cards"]]
        hasMore = data["hasMore"]

    while hasMore and utils.maybeHappen():
        data = UserReqs.userCards(session, userId, last=cardIds[-1])
        if data:
            cardIds.extend([card["id"] for card in data["cards"]])
            hasMore = data["hasMore"]
        else:
            hasMore = False

    boxIds, hasMore = [], False
    data = UserReqs.userBoxes(session, userId)
    if data:
        boxIds = [box["id"] for box in data["boxes"]]
        hasMore = data["hasMore"]

    while hasMore and utils.maybeHappen():
        data = UserReqs.userBoxes(session, userId, last=boxIds[-1])
        if data:
            boxIds.extend([box["id"] for box in data["boxes"]])
            hasMore = data["hasMore"]
        else:
            hasMore = False

    backpackIds = []
    backpacks = UserReqs.userBackpacks(session, userId)
    if backpacks:
        backpackIds = [backpack["id"] for backpack in backpacks]

    return {"cards": cardIds, "boxes": boxIds, "backpacks": backpackIds}


def userLogin(session, email, password):
    token = UserReqs.authLogin(session, email, password) or \
        UserReqs.authRegister(session, email, password)

    return token
