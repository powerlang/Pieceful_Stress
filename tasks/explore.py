import random
from gevent.local import local
from locust import TaskSet, task
from reqs import ExploreReqs
from behavior import newCard, cardDetail
import utils
import logging
console_logger = logging.getLogger("console_logger")
stash = local()


class ExploreTaskSet(TaskSet):

    @task(20)
    def cardDetail(self):
        if stash.cardIds:
            cardDetail(self.client, random.choice(stash.cardIds))

    @task(10)
    def newCard(self):
        if not utils.isAnonymous(self.client):
            newCard(self.client)

    @task(5)
    def stop(self):
        self.interrupt()

    def on_start(self):
        exploreData = ExploreReqs.exploreCards(self.client)
        stash.cardIds = exploreData.get("cardIds", [])
        stash.userIds = exploreData.get("userIds", [])
        stash.boxIds = exploreData.get("boxIds", [])
