from locust import HttpUser, task

class BlazeMeterUser(HttpUser):
    @task
    def blaze_task(self):
        self.client.get("/", name="BlazeMeter GET")

class TricentisUser(HttpUser):
    @task
    def tricentis_task(self):
        self.client.get("/", name="Tricentis GET")
