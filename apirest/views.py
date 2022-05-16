from rest_framework import generics
from django.db.models import Count, Case, When, Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from drf_yasg.utils import swagger_auto_schema

from apirest.models import Reviews
from apirest.permissions import IsOwnerOrReadOnly
from apirest.serializers import NukuraSerializer, UserStoreRelationSerializer, CommentsSerializer, CustomUserSerializer, \
    CompanySerializer
from nukura.models import NukuraStore, UserStoreRelation
from users.models import CustomUser, Company


class NukuraViewSet(ModelViewSet):

    queryset = NukuraStore.objects.all().annotate(
            annotated_likes=Count(Case(When(userstorerelation__like=True, then=1))),
           ).select_related('categ').select_related('owner').prefetch_related('readers').order_by('id')
    serializer_class = NukuraSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    filter_fields = ['price']
    search_fields = ['name', 'author_name']
    ordering_fields = ['price', 'author_name']

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class UserBooksRelationView(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserStoreRelation.objects.all()
    serializer_class = UserStoreRelationSerializer
    lookup_field = 'store'

    def get_object(self):
        obj, _ = UserStoreRelation.objects.get_or_create(user=self.user,
                                                        store_id=self.kwargs['store'])

        return obj


class CommentsView(ModelViewSet):
    serializer_class = CommentsSerializer
    queryset = Reviews.objects.all()
    permission_classes = [AllowAny]


class CustomUserViewSet(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]


class CompanyViewSet(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [AllowAny]
