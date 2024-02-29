# Create your tests here.
from django.test import TestCase
from django.test.client import Client

from jumpmetric.models import Trial


class TestTrial(TestCase):
    def test_setUp(self) -> None:
        fullnames = [
            "fullname", "190", "89", "29", "test@test.test", "studentTest", "CMJ", "10", "filenameTEst"
        ]
        for item in fullnames:
            Trial.objects.create(fullname=item, height=item, weight=item, age=item, email=item, occupy=item, type_of_trial=item, drop_jump_height=item, filename=item)

    # def test_list_todo(self):
    #     c = Client()
    #     response = c.get("")
    #     self.assertEqual(response.status_code, 200)
    #     count = len(response.json().get("data"))
    #     self.assertEqual(count, 2)

    # def test_create_todo(self):
    #     c = Client()
    #     response = c.post("/create/", {
    #         "fullname": "fullnametest"
    #     })
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(
    #         response.json().get("trial"), "fullnametest"
    #     )

    # def test_retrieve_todo(self):
    #     c = Client()
    #     response = c.get("/retrieve/1/", {
    #         "task": "New task"
    #     })
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(
    #         response.json().get("todo"), "test"
    #     )

    # def test_update_todo(self):
    #     c = Client()
    #     response = c.post("/update/1/", {
    #         "task": "test updated task",
    #         "done": True
    #     })
    #     self.assertEqual(response.status_code, 200)
    #     data = response.json()
    #     result_todo = data.get("todo")
    #     result_done = data.get("done")
    #     self.assertEqual(
    #         result_todo, "test updated task"
    #     )
    #     self.assertEqual(result_done, True)
    #     todo_obj = TodoM.objects.get(id=1)
    #     self.assertEqual(todo_obj.done, True)

    # def test_delete_todo(self):
    #     c = Client()
    #     response = c.delete("/delete/1/")
    #     self.assertEqual(response.status_code, 204)