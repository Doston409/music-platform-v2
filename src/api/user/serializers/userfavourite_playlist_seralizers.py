from rest_framework.serializers import ModelSerializer
from apps.users.models import Favouriteplaylist
from rest_framework.exceptions import ValidationError

class FavouriteplaylistListSeralizer(ModelSerializer):

    class Meta:
        model = Favouriteplaylist
        fields = '__all__'


class FavouriteplaylistCreateSeralizer(ModelSerializer):

    class Meta:
        model = Favouriteplaylist
        fields = '__all__'

    

    def validate_playlist(self, playlist):
         
        favourite = Favouriteplaylist.objects.filter(user=self.user, music=playlist)
        if favourite.exists():
            raise ValidationError("this music alredy exists in your favourite list")
        elif not playlist.is_public:
            raise ValidationError("You cen't add playlist to you favourite")
        return playlist
