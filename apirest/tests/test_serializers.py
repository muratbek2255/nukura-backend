import io

from django.contrib.auth.models import User
from django.core.files.images import ImageFile
from django.db.models import Count, Case, When, Avg
from django.test import TestCase

from apirest.serializers import NukuraSerializer
from nukura.models import NukuraStore, UserStoreRelation


class NukuraTestSerializer(TestCase):
    def test_ok(self):
        user1 = User.objects.create(username='user1')
        user2 = User.objects.create(username='user2')
        user3 = User.objects.create(username='user3')

        first_product = NukuraStore.objects.create(title='Mucho gracios',
                                                   image=ImageFile(io.BytesIO(b'some-file'), name='test-image.jpg'),
                                                   price=20000.00, author_name='User')
        UserStoreRelation.objects.create(user=user1, store=first_product, like=True,
                                        rate=5)

        store = NukuraStore.objects.all().annotate(
            annotated_likes=Count(Case(When(userstorerelation__like=True, then=1))),
            rating=Avg('userstorerelation__rate')
        ).order_by('id')
        srz=NukuraSerializer(store, many=False).data
        excepted = [{
            'id': first_product.id,
            'title': 'Mucho gracios',
            'image' : ImageFile(io.BytesIO(b'some-file'), name='test-image.jpg'),
            'price': '20000.00',
            'author_name': 'User',
            'likes_count': 3,
            'annotated_likes': 3,
            'rating': '4.67'
        }
        ]
        self.assertEqual(excepted, srz)