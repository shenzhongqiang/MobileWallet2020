from django.test import TestCase
from mainapp.models import User, Transaction, Usage
from mainapp.views import list_users

# Create your tests here.
class UserTest(TestCase):
    def setUp(self):
        User.objects.create(username="testuser", password="testpwd")

    def test_balance(self):
        user = User.objects.get(username="testuser")
        self.assertEqual(user.balance, 0)

class TransactionTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="user1", password="testpwd", balance=200)
        self.user2 = User.objects.create(username="user2", password="testpwd", balance=100)
        Transaction.objects.create(from_user=self.user1, to_user=self.user2, amount=100)

    def test_amount(self):
        transacs = Transaction.objects.filter(from_user=self.user1)
        self.assertEqual(transacs.count(), 1)

class UsageTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="user1", password="testpwd", balance=200)
        Usage.objects.create(api_func="list_users", user=self.user1)

    def test_api_name(self):
        usages = Usage.objects.filter(user=self.user1)
        self.assertEqual(usages.count(), 1)
        usage = usages[0]
        self.assertEqual(usage.api_name, "/api/users/")
