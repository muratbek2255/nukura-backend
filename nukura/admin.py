from django.contrib import admin

from nukura.models import NukuraStore, UserStoreRelation, Category
from apirest.models import Reviews
from users.models import CustomUser, Company, EcoCompany


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


@admin.register(CustomUser)
class ReviewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(EcoCompany)
class EcoCompanyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        gender_count = EcoCompany.objects.all().count()
        if gender_count >= 2:
            return False
        else:
            return True
