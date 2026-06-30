from django.db.models.signals import post_save,m2m_changed
from django.dispatch import receiver
from mutagen.mp3 import MP3
from mutagen.wave import WAVE


from .models import Music,Playlist



@receiver(post_save,sender=Music)
def update_music_duration(sender,instance, cerated,**kwargs):
    if cerated and instance.music_date:
        try:
