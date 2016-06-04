import random
import utils


def exploreCards(session):
    data = {}
    endPage = random.randint(0, 9)
    for page in range(endPage + 1):
        r = session.get("/explore/?start={}".format(24*page), name="/explore")

        cards = utils.getResData(r, "cards")
        if not cards:
            break

        data.setdefault("cardIds", []).extend([card["id"] for card in cards])
        data.setdefault("userIds", []).extend([card["owner"]["id"] for card in cards])
        data.setdefault("boxIds", []).extend([card["box"]["id"] for card in cards if card.get("box")])

    return data
