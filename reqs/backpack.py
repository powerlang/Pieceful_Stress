import utils


def backpackContent(session, backpackId):
    r = session.get("/backpack/{}/content/".format(backpackId), name="/backpack/[id]/content")
    return utils.getResData(r)


def backpackInfo(session, backpackId):
    r = session.get("/backpack/{}/info/".format(backpackId), name="/backpack/[id]/info")
    return utils.getResData(r, "backpack")


def backpackDetail(session, backpackId):
    r = session.get("/backpack/{}/content-details/".format(backpackId), name="/backpack/[id]/content-details")
    return utils.getResData(r)


def backpackMemos(session, backpackId):
    r = session.get("/backpack/{}/memos/".format(backpackId), name="/backpack/[id]/memos")
    return utils.getResData(r, "memos")


def backpackSchedule(session, backpackId):
    r = session.get("/backpack/{}/schedule/".format(backpackId), name="/backpack/[id]/schedule")
    return utils.getResData(r, "schedule")


def backpackRoute(session, backpackId):
    r = session.get("/backpack/{}/route/".format(backpackId), name="/backpack/[id]/route")
    return utils.getResData(r, "route")


def backpackDestinationTransit(session, backpackId, destinationId):
    r = session.get("/backpack/{}/destination/{}/transit/".format(backpackId, destinationId), name="/backpack/[id]/destination/[id]/transit")
    return utils.getResData(r, "transit")


def backpackTransit(session, backpackId):
    r = session.get("/backpack/{}/transit/".format(backpackId), name="/backpack/[id]/transit")
    return utils.getResData(r, "transit")


def backpackTransitInfo(session, backpackId, transitId):
    r = session.get("/backpack/{}/transit/{}/".format(backpackId, transitId), name="/backpack/[id]/transit/[id]")
    return utils.getResData(r)


def backpackDestinationStay(session, backpackId, destinationId):
    r = session.get("/backpack/{}/destination/{}/stay/".format(backpackId, destinationId), name="/backpack/[id]/destination/[id]/stay/")
    return utils.getResData(r, "stay")


def backpackStay(session, backpackId):
    r = session.get("/backpack/{}/stay/".format(backpackId), name="/backpack/[id]/stay/")
    return utils.getResData(r, "stay")


def backpackStayInfo(session, backpackId, stayId):
    r = session.get("/backpack/{}/stay/{}/".format(backpackId, stayId), name="/backpack/[id]/stay/[id]")
    return utils.getResData(r)


def backpackDestinationPlaces(session, backpackId, destinationId):
    r = session.get("/backpack/{}/destination/{}/places/".format(backpackId, destinationId), name="/backpack/[id]/destination/[id]/places")
    return utils.getResData(r)


def backpackAgendaInfo(session, backpackId, dayId):
    r = session.get("/backpack/{}/agenda/{}/".format(backpackId, dayId), name="/backpack/[id]/agenda/[id]")
    return utils.getResData(r)


def backpackAgenda(session, backpackId):
    r = session.get("/backpack/{}/agenda/".format(backpackId), name="/backpack/[id]/agenda")
    return utils.getResData(r, "agenda")


def backpackAgendaDay(session, backpackId, dayId):
    r = session.get("/backpack/{}/agenda-day/{}/".format(backpackId, dayId), name="/backpack/[id]/agenda-day/[id]")
    return utils.getResData(r)


def backpackFull(session, backpackId):
    r = session.get("/backpack/{}/full/".format(backpackId), name="/backpack/[id]/full")
    return utils.getResData(r)


def backpackMemoInfo(session, backpackId, memoId):
    r = session.get("/backpack/{}/memo/{}/".format(backpackId, memoId), name="/backpack/[id]/memo/[id]")
    return utils.getResData(r)


def backpackClone(session, backpackId):
    r = session.put("/backpack/{}/clone/".format(backpackId), name="/backpack/[id]/clone")
    return utils.getResData(r, "cloned")


def backpackCloned(session, backpackId):
    r = session.get("/backpack/{}/clone/".format(backpackId), name="/backpack/[id]/clone")
    return utils.getResData(r, "cloned")
