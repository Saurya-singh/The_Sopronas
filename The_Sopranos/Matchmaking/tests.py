from django.test import TestCase
from Matchmaking.models import Status,User
# Create your tests here.

class Setup_Test(TestCase):
    def setUp(self):
        statobj = Status.objects.create(fullname = "Ram", yourpost = "my post less than20")
        Userobj = User.objects.create(user_name = "Ram", user_email = "nilesh@gmail.com", user_address= "kalopool", user_gender="female",user_age= "20" )
    
    def test_valid(self):
        statobj = Status.objects.get(fullname = "Ram")
        value = statobj.valid()
        self.assertTrue(value,True)


    def test_valid_postlength(self):
        statobj = Status.objects.get(fullname = "Ram")
        value  = statobj.length()
        self.assertTrue(value,True)

    def test_valid_username(self):
        obj = User.objects.get(user_name = "Ram")
        value  = obj.valid_name()
        self.assertTrue(value,True)

    def test_valid_gender(self):
        obj = User.objects.get(user_name = "Ram")
        value  = obj.valid_gender()
        self.assertTrue(value,True)

    def test_valid_age(self):
        obj = User.objects.get(user_name = "Ram")
        value  = obj.valid_age()
        self.assertTrue(value,True)





