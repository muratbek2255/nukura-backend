from django.db import models
from users.models import CustomUser, Company


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
    description = models.TextField(default='Its cool')
    owner = models.ForeignKey(Company, on_delete=models.SET_NULL,
                              null=True, related_name='my_books')
    author_name = models.CharField(max_length=255, default='Murat')
    readers = models.ManyToManyField(to=CustomUser, through='UserStoreRelation', related_name='store')

    def __str__(self):
        return f'{self.id}: {self.title}'


class UserStoreRelation(models.Model):
    RATE_CHOICES = (
        (1, 'Ok'),
        (2, 'Fine'),
        (3, 'Good'),
        (4, 'Amazing'),
        (5, 'Incredible')
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    store = models.ForeignKey(NukuraStore, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_storemarks = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return f' {self.user}: {self.store}, RATE {self.rate}'

    def save(self, *args, **kwargs):
        from apirest.logic import set_rating

        creating = not self.pk
        old_rating = self.rate

        super().save(*args, **kwargs)

        new_rating = self.rate
        if old_rating != new_rating or creating:
            set_rating(self.store)
