from locust import HttpLocust, events

import utils
from tasks import ExploreTaskSet


def resetUsersHandler():
    utils.clearUsers("explore")


events.locust_start_hatching += resetUsersHandler

class LushuLocust(HttpLocust):
    task_set = ExploreTaskSet
    weight = 30
    min_wait = 10
    max_wait = 150


# class LushuTripLocust(HttpLocust):
#     task_set = TripTaskSet
#     weight = 10
#     min_wait = 1000
#     max_wait = 1000
