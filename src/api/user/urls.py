from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.user.views import music_views, playlist_views, favourite_music, favourite_playlist_views

router = DefaultRouter()
router.include_root_view = False

urlpatterns = [
    # music
    path('music/', music_views.MusicListApiView.as_view()),
    path('music/create/', music_views.MusicCreateAPIView.as_view()),
    path('music/detail/<int:pk>/', music_views.MusicRetrieveAPIView.as_view()),
    path('music/detail/<int:pk>/', music_views.MusicDestroyAPIView.as_view()),
    path('music/detail/<int:pk>/', music_views.MusicUpdateAPIView.as_view()),

    # playlist
    path('playlist/', playlist_views.PlaylistListApiView.as_view()),
    path('playlist/create/', playlist_views.PlaylistCreateAPIView.as_view()),
    path('playlist/detail/<int:pk>/', playlist_views.PlaylistRetrieveAPIView.as_view()),
    path('playlist/detail/<int:pk>/', playlist_views.PlaylistDestroyAPIView.as_view()),
    path('playlist/detail/<int:pk>/', playlist_views.PlaylistUpdateAPIView.as_view()),

    # user favourite
    path('favourite/', favourite_music.FavouriteListApiView.as_view()),
    path('favourite/create/', favourite_music.FavouriteCreateAPIView.as_view()),
    path('favourite/detail/<int:pk>/', favourite_music.FavouriteRetrieveAPIView.as_view()),
    path('favourite/detail/<int:pk>/', favourite_music.FavouriteDestroyAPIView.as_view()),
    path('favourite/detail/<int:pk>/', favourite_music.FavouriteUpdateAPIView.as_view()),

    # user favourite playlist
    path('favourite-palylist/', favourite_playlist_views.FavouriteplaylistListApiView.as_view()),
    path('favourite-palylist/create/', favourite_playlist_views.FavouriteplaylistCreateAPIView.as_view()),
    path('favourite-palylist/detail/<int:pk>/', favourite_playlist_views.FavouriteplaylistRetrieveAPIView.as_view()),
    path('favourite-palylist/detail/<int:pk>/', favourite_playlist_views.FavouriteplaylistDestroyAPIView.as_view()),
    path('favourite-palylist/detail/<int:pk>/', favourite_playlist_views.FavouriteplaylistUpdateAPIView.as_view()),


    # path('', include(router.urls)),
    # path('restaurant/', RestaurantViewset.as_view({'get': 'list','post':'create'}), name='restaurant-detail'),
]
