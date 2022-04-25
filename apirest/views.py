from django.db.models import Count, Case, When, Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from drf_yasg.utils import swagger_auto_schema

from apirest.models import Reviews
from apirest.permissions import IsOwnerOrReadOnly
from apirest.serializers import NukuraSerializer, UserStoreRelationSerializer, CommentsSerializer
from nukura.models import NukuraStore, UserStoreRelation


class NukuraViewSet(ModelViewSet):

    queryset = NukuraStore.objects.all().annotate(
            annotated_likes=Count(Case(When(userstorerelation__like=True, then=1))),
           ).select_related('cat').select_related('owner').prefetch_related('readers').order_by('id')
    serializer_class = NukuraSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsOwnerOrReadOnly]
    filter_fields = ['price']
    search_fields = ['name', 'author_name']
    ordering_fields = ['price', 'author_name']

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class UserRelationView(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = UserStoreRelation.objects.all()
    serializer_class = UserStoreRelationSerializer
    lookup_field = 'store'

    def get_object(self):
        obj, _ = UserStoreRelation.objects.get_or_create(user=self.request.user,
                                                        store_id=self.kwargs['book'])

        return obj


class CommentsView(ModelViewSet):
    serializer_class = CommentsSerializer
    queryset = Reviews.objects.all()
    permission_classes = [IsAuthenticated]