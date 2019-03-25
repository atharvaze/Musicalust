from django.contrib import admin

# Register your models here.
from .models import Album, Song

admin.site.register(Album) #to make the music class appear on admin page
admin.site.register(Song)
