from rest_framework.generics import ListAPIView,\
    CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from api.user.serializers import userfavourite_seralizers
from rest_framework import status
from rest_framework.response import Response
from apps.users.models import Favourite


class FavouriteListApiView(ListAPIView):
    queryset = Favourite.objects.all()
    serializer_class = userfavourite_seralizers.FavouriteListSeralizer
    permission_classes = [IsAuthenticated]


class FavouriteCreateAPIView(CreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = userfavourite_seralizers.FavouriteCreateSeralizer
    permission_classes = [IsAuthenticated]


class FavouriteUpdateAPIView(UpdateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = userfavourite_seralizers.FavouriteCreateSeralizer
    permission_classes = [IsAuthenticated]


class FavouriteRetrieveAPIView(RetrieveAPIView):
    queryset = Favourite.objects.all()
    serializer_class = userfavourite_seralizers.FavouriteListSeralizer
    permission_classes = [IsAuthenticated]


class FavouriteDestroyAPIView(DestroyAPIView):
    queryset = Favourite.objects.all()
    permission_classes = [IsAuthenticated]


