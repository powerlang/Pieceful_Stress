import random
from locust import HttpLocust, TaskSet

import config
import utils
from reqs import UserReqs
from tasks import ExploreTaskSet


class LushuTaskSet(TaskSet):
    tasks = {ExploreTaskSet: 10}

    def on_start(self):
        if utils.maybeHappen():
            return

        email = random.choice(config.FAKE_EMAILS)
        password = config.FAKE_USER_PASSWORD
        token = UserReqs.authLogin(self.client, email, password) or \
            UserReqs.authRegister(self.client, email, password)

        if token:
            self.client.headers["Authorization"] = "Token {}".format(token)


class LushuLocust(HttpLocust):
    task_set = LushuTaskSet
    min_wait = 5000
    max_wait = 15000
