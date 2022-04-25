from django.db.models import Avg

from nukura.models import UserStoreRelation


def set_rating(store):
    rating = UserStoreRelation.objects.filter(store=store).aggregate(rating=Avg('rate')).get('rating')
    store.rating = rating
    store.save()