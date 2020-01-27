from django.test import TestCase
from Matchmaking.models import Status
# Create your tests here.

class Setup_Test(TestCase):
    def setUp(self):
        statobj = Status.objects.create(fullname = "Ram", yourpost = "my post less than20")

    def test_valid(self):
        statobj = Status.objects.get(fullname = "Ram")
        value = statobj.valid()
        self.assertTrue(value,True)


    def test_valid_postlength(self):
        statobj = Status.objects.get(fullname = "Ram")
        value  = statobj.length()
        self.assertTrue(value,True)




