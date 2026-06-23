from rest_framework.generics import ListAPIView,\
    CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from api.user.serializers import music_seralizers
from rest_framework import status
from rest_framework.response import Response
from apps.music.models import Music





class HomeTopMusicListApiView(ListAPIView):
    queryset = Music.objects.filter(is_public=True)
    serializer_class = music_seralizers.MusicListSeralizer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset



class HomeTopMusicListApiView(ListAPIView):
    queryset = Music.objects.filter(is_public=True)
    serializer_class = music_seralizers.PlaylistSeralizers
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset



    #     if self.is_mine:
    #         queryset =  Music.objects.filter(author=self.request.user)
    #     if self.playlist:
    #         try: playlist = list(map(lambda d: int(d), self.playlist.split(",")))
    #         except: return []
    #         queryset = queryset.filter(playlist__id__in=playlist).distinct()
    #     return queryset

    # def list(self, request, *args, **kwargs):
    #     self.is_mine =  request.GET.get("is_mine", False)
    #     self.playlist = request.GET.get("playlist", False)
    #     return super().list(request, *args, **kwargs)

