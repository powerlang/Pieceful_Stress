import gevent
import random
from reqs import CardReqs, UserReqs, BoxReqs, SearchReqs
import utils


def newCard(session):
    account = UserReqs.authRefreshStatus(session)
    if not account:
        return

    userId = account["id"]
    boxId = None
    result = UserReqs.userBoxes(session, userId)
    if result and result["boxes"] and utils.maybeHappen():
        boxId = random.choice(result["boxes"])["id"]

    if boxId is None and utils.maybeHappen():
        box = BoxReqs.newBox(session, {})
        if box:
            boxId = box["id"]

    cardData = {"boxId": boxId}

    places = SearchReqs.searchPlaces(session, utils.randomWord(), 0)
    if places:
        selectedPlaces = [random.choice(places) for i in range(random.randint(1, len(places)))]
        destinations = [place["destination"] for place in selectedPlaces if "destination" in place]
        destinationId = destinations[0]["id"] if destinations else None
        poiIds = [place["poi"]["id"] for place in selectedPlaces] if not destinationId else None
        if destinationId:
            cardData.update({"type": 2, "destination": destinationId})
        elif poiIds:
            cardData.update({"type": 1, "pois": "|".join(list(set(poiIds)))})

    CardReqs.newCard(session, cardData)


def cardDetail(session, cardId):
    result = {"cards": [], "boxes": [], "pois": [], "destinations": []}

    card = CardReqs.getCard(session, cardId)
    if not card:
        return result

    if card.get("pois"):
        result["pois"] = [poi["id"] for poi in card["pois"]]

    if card.get("destination"):
        result["destinations"] = [card["destination"]["id"]]

    CardReqs.getCardComments(session, cardId)
    cards = CardReqs.getRelatedCards(session, cardId)
    if cards:
        result["cards"] = [card["id"] for card in cards]

    boxes = CardReqs.getRelatedBoxes(session, cardId)
    if boxes:
        result["boxes"] = [box["id"] for box in boxes]

    if utils.isAnonymous(session):
        return result

    followed = UserReqs.userFollowed(session, card["owner"]["id"])
    if not followed and utils.rarelyHappen():
        gevent.sleep(1)
        UserReqs.followUser(session, card["owner"]["id"])

    if not card["liked"] and utils.rarelyHappen():
        gevent.sleep(1)
        CardReqs.likeCard(session, cardId)

    account = UserReqs.authRefreshStatus(session)
    if not account:
        return result

    if not card["clipped"] and utils.rarelyHappen():
        gevent.sleep(1)

        userId = account["id"]
        boxId = None
        data = UserReqs.userBoxes(session, userId)
        if data and data["boxes"] and utils.maybeHappen():
            boxId = random.choice(data["boxes"])["id"]

        if boxId is None and utils.maybeHappen():
            box = BoxReqs.newBox(session, {})
            if box:
                boxId = box["id"]

        CardReqs.clipCard(session, cardId, boxId)

    return result
