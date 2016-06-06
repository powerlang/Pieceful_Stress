from reqs import BackpackReqs
import utils


def backpackPage(session, backpackId):
    result = {"cards": [], "pois": [], "destinations": []}

    data = BackpackReqs.backpackDetail(session, backpackId)
    if not data:
        return result

    content = data["content"]

    if content.get("poiCards"):
        result["cards"] = [card["id"] for poiCard in content["poiCards"] if poiCard for card in poiCard.get("cards", [])]
        result["pois"] = [poiCard["poi"]["id"] for poiCard in content["poiCards"] if poiCard]

    if content.get("destinationCards"):
        result["cards"].extend([card["id"] for destinationCard in content.get("destinationCards", []) for card in destinationCard.get("cards", [])])
        result["destinations"] = [city["city"]["id"] for destinationCard in content.get("destinationCards", []) for city in destinationCard.get("cities", [])]

    if utils.isAnonymous(session):
        return result

    if utils.maybeHappen():
        cloned = BackpackReqs.backpackCloned(session, backpackId)
        if not cloned:
            BackpackReqs.backpackClone(session, backpackId)

    return result
