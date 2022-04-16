import io

from django.core.files.images import ImageFile
from rest_framework.test import APITestCase
from django.urls import reverse

from apirest.serializers import NukuraSerializer
from nukura.models import NukuraStore


class NukuraApiTestCase(APITestCase):
    def test_get(self):
        first_product = NukuraStore.objects.create(title='Mucho gracios', image=ImageFile(io.BytesIO(b'some-file'), name='test-image.jpg'),
                                                   price=20000, author_name='User')
        url = reverse('nukurastore-list')
        print(url)
        response = self.client.get(url)
        print(response.data)