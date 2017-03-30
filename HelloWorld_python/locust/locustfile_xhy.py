from locust import HttpLocust, TaskSet, task

class locustfile_x(TaskSet):


    @task(1)
    def index(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):

    task_set = locustfile_x
    min_wait = 0
    max_wait = 0