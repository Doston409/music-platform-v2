from rest_framework.generics import ListAPIView,\
    CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from api.user.serializers import playlist_seralizers,music_seralizers
from rest_framework import status
from rest_framework.response import Response
from apps.music.models import Music
from rest_framework.viewsets import ModelViewSet
from api.user.permissions import CustomPermissions



class TestAPiViewset(ModelViewSet):
    serializer_class = music_seralizers.MusicListSeralizer
    queryset = Music.objects.all()
    permission_classes = [IsAuthenticated,CustomPermissions]

    def list(self, request, *args, **kwargs):
        print(request.user)
        return super().list(request, *args, **kwargs)
    

class HomeTopMusicListApiView(ListAPIView):
    queryset = Music.objects.filter(is_public=True)
    serializer_class = music_seralizers.MusicListSeralizer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset



class HomeTopMusicListApiView(ListAPIView):
    queryset = Music.objects.filter(is_public=True)
    serializer_class = playlist_seralizers.PlaylistListSeralizer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset



 