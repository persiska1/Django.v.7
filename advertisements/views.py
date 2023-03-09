# from rest_framework.permissions import IsAuthenticated
# from rest_framework.viewsets import ModelViewSet
#
#
# class AdvertisementViewSet(ModelViewSet):
#     """ViewSet для объявлений."""
#
#     # TODO: настройте ViewSet, укажите атрибуты для кверисета,
#     #   сериализаторов и фильтров
#
#     def get_permissions(self):
#         """Получение прав для действий."""
#         if self.action in ["create", "update", "partial_update"]:
#             return [IsAuthenticated()]
#         return []


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.filter()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend,]
    filter_class = AdvertisementFilter



    def get_permissions(self):
        return [IsAuthenticatedOrReadOnly(), IsOwner()]
