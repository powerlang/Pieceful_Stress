import requests
from gevent.local import local
from locust import TaskSet, task
from behavior import (CardBehavior, UserBehavior, BoxBehavior, BackpackBehavior,
                      PoiBehavior, DestinationBehavior, ExploreBehavior)
import utils
import logging
console_logger = logging.getLogger("console_logger")
stash = local()


class ExploreTaskSet(TaskSet):

    @task(80)
    def cardDetail(self):
        if stash.cardIds:
            cardId = utils.weightedChoice(stash.cardIds)
            utils.ajustWeight(stash.cardIds, cardId)
            result = CardBehavior.cardDetail(self.client, cardId)
            utils.statWeight(stash.cardIds, result["cards"])
            utils.statWeight(stash.boxIds, result["boxes"])
            if result.get("pois"):
                utils.statWeight(stash.poiIds, result["pois"])
            if result.get("destinations"):
                utils.statWeight(stash.destinationIds, result["destinations"])

    @task(20)
    def userHome(self):
        if stash.userIds:
            userId = utils.weightedChoice(stash.userIds)
            utils.ajustWeight(stash.userIds, userId)
            result = UserBehavior.userHome(self.client, userId)
            utils.statWeight(stash.cardIds, result["cards"])
            utils.statWeight(stash.boxIds, result["boxes"])
            utils.statWeight(stash.backpackIds, result["backpacks"])

    @task(20)
    def boxHome(self):
        if stash.boxIds:
            boxId = utils.weightedChoice(stash.boxIds)
            utils.ajustWeight(stash.boxIds, boxId)
            result = BoxBehavior.boxHome(self.client, boxId)
            utils.statWeight(stash.cardIds, result["cards"])

    @task(10)
    def newCard(self):
        if not utils.isAnonymous(self.client):
            CardBehavior.newCard(self.client)

    @task(10)
    def poiDetail(self):
        if stash.poiIds:
            poiId = utils.weightedChoice(stash.poiIds)
            utils.ajustWeight(stash.poiIds, poiId)
            result = PoiBehavior.poiDetail(self.client, poiId)
            utils.statWeight(stash.cardIds, result["cards"])
            utils.statWeight(stash.poiIds, result["pois"])

    @task(10)
    def destinationDetial(self):
        if stash.destinationIds:
            destId = utils.weightedChoice(stash.destinationIds)
            utils.ajustWeight(stash.destinationIds, destId)
            result = DestinationBehavior.destinationDetial(self.client, destId)
            utils.statWeight(stash.cardIds, result["cards"])
            utils.statWeight(stash.userIds, result["users"])
            utils.statWeight(stash.boxIds, result["boxes"])

    @task(10)
    def backpack(self):
        if stash.backpackIds:
            backpackId = utils.weightedChoice(stash.backpackIds)
            utils.ajustWeight(stash.backpackIds, backpackId)
            result = BackpackBehavior.backpackPage(self.client, backpackId)
            utils.statWeight(stash.cardIds, result["cards"])
            utils.statWeight(stash.poiIds, result["pois"])
            utils.statWeight(stash.destinationIds, result["destinations"])

    @task(5)
    def index(self):
        self.explore(self.client)

    @classmethod
    def explore(cls, session):
        exploreData = ExploreBehavior.index(session)
        stash.cardIds = {}
        stash.poiIds = {}
        stash.destinationIds = {}
        stash.userIds = {}
        stash.boxIds = {}
        stash.backpackIds = {}
        utils.statWeight(stash.cardIds, exploreData.get("cardIds", []))
        utils.statWeight(stash.userIds, exploreData.get("userIds", []))
        utils.statWeight(stash.boxIds, exploreData.get("boxIds", []))

    def on_start(self):
        a = requests.adapters.HTTPAdapter(max_retries=3)
        self.client.mount('http://', a)

        if utils.maybeHappen():
            user = utils.getNextUser("explore")
            token = UserBehavior.userLogin(self.client, user["email"], user["password"])
            if token:
                self.client.headers["Authorization"] = "Token {}".format(token)

        self.explore(self.client)
