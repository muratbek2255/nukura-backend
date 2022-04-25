from django.db import models
from users.models import CustomUser


class Category(models.Model):
    """Категория"""
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title


class NukuraStore(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(default='image/burger-2.jpg')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    categ = models.ForeignKey(Category, on_delete=models.SET_NULL,blank=True, null=True,  related_name='cat')
    author_name = models.CharField(max_length=255, default='Murat')
    readers = models.ManyToManyField(to=CustomUser, through='UserStoreRelation', related_name='store')

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



