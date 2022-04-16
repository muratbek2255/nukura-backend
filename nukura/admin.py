from django.contrib import admin

from nukura.models import NukuraStore, UserStoreRelation


@admin.register(NukuraStore)
class NukuraAdmin(admin.ModelAdmin):
    pass


@admin.register(UserStoreRelation)
class NukuraAdmin(admin.ModelAdmin):
    pass