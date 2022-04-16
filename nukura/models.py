from django.contrib.auth.models import User
from django.db import models

from users.models import CustomUser


class NukuraStore(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(default='image/burger-2.jpg')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author_name = models.CharField(max_length=255, default='Murat')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='mystore')
    readers = models.ManyToManyField(CustomUser, through='UserStoreRelation', related_name='store')

    def __str__(self):
        return f'{self.id}: {self.title}'


class UserStoreRelation(models.Model):
    RATE_CHOICES = (
        (1, 'OK'),
        (2, 'FINE'),
        (3, 'GOOD'),
        (4, 'AMAZING'),
        (5, 'INCREDIBLE')
    )


    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    store = models.ForeignKey(NukuraStore, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_storemarks = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return f'{self.id}: {self.user}, ТОВАР:{self.store}, RATE: {self.rate}'