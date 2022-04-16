from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from nukura.models import NukuraStore, UserStoreRelation


class NukuraSerializer(ModelSerializer):
    # likes_count = serializers.SerializerMethodField()

    annotated_likes = serializers.IntegerField(read_only=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2)
    owner_name = serializers.CharField(source='owner.username', default="", read_only=True)

    class Meta:
        model = NukuraStore
        fields = ('id', 'title', 'price', 'author_name',  'annotated_likes', 'rating', 'owner_name')

    # def get_likes_count(self, instance):
    #     return UserStoreRelation.objects.filter(store=instance, like=True).count()


class UserStoreRelationSerializer(ModelSerializer):
    class Meta:
        model = UserStoreRelation
        fields = ('store', 'like', 'in_storemarks', 'rate')