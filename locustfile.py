from locust import HttpUser, between, task


import time
from locust import HttpUser, task, between
class QuickstartUser(HttpUser):
  wait_time = between(1, 2.5) # Range of seconds per user on page

  @task
  def hello_world(self):
    self.client.get("/")
    self.client.get("/other")

  @task(3) # Number is task weights
  def view_items(self):
    for value_no in range(10):
      self.client.get(f"/exp?value={value_no}")
    time.sleep(1)
