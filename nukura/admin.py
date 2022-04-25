from django.contrib import admin

from nukura.models import NukuraStore, UserStoreRelation, Category
from apirest.models import Reviews


@admin.register(NukuraStore)
class NukuraAdmin(admin.ModelAdmin):
    pass


@admin.register(UserStoreRelation)
class NukuraAdmin(admin.ModelAdmin):
    pass


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class ReviewsAdmin(admin.ModelAdmin):
    pass