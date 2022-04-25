from django.contrib.auth.models import User
from django.test import TestCase

from apirest.logic import set_rating
from nukura.models import NukuraStore, UserStoreRelation
from users.models import CustomUser


class SetRatingTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(username='user1',
                                    first_name='Ivan', last_name='Petrov')
        user2 = User.objects.create(username='user2',
                                    first_name='Ivan', last_name='Sidorov')
        user3 = User.objects.create(username='user3',
                                    first_name='1', last_name='2')


        self.book_1 = NukuraStore.objects.create(name='Test book 1', price=25,
                                          author_name='Author 1', owner=user1)



    def test_ok(self):
        set_rating(self.book_1)

        self.assertEqual('4.67', str(self.book_1.rating))
