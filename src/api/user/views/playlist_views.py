from rest_framework.generics import ListAPIView,\
    CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from api.user.serializers import playlist_seralizers
from rest_framework import status
from rest_framework.response import Response
from apps.music.models import Playlist


class PlaylistListApiView(ListAPIView):
    queryset = Playlist.objects.all()
    serializer_class = playlist_seralizers.PlaylistListSeralizer
    permission_classes = [IsAuthenticated]


class PlaylistCreateAPIView(CreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = playlist_seralizers.PlaylistCreateSeralizer
    permission_classes = [IsAuthenticated]


class PlaylistUpdateAPIView(UpdateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = playlist_seralizers.PlaylistCreateSeralizer
    permission_classes = [IsAuthenticated]


class PlaylistRetrieveAPIView(RetrieveAPIView):
    queryset = Playlist.objects.all()
    serializer_class = playlist_seralizers.PlaylistListSeralizer
    permission_classes = [IsAuthenticated]


class PlaylistDestroyAPIView(DestroyAPIView):
    queryset = Playlist.objects.all()
    permission_classes = [IsAuthenticated]


