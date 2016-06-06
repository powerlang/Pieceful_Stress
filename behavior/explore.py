import random
from reqs import ExploreReqs


def index(session):
    data = {}
    endPage = random.randint(0, 5)
    for page in range(endPage + 1):
        cards = ExploreReqs.exploreCards(session, page)
        if not cards:
            break

        data.setdefault("cardIds", []).extend([card["id"] for card in cards])
        data.setdefault("userIds", []).extend([card["owner"]["id"] for card in cards])
        data.setdefault("boxIds", []).extend([card["box"]["id"] for card in cards if card.get("box")])

    return data
