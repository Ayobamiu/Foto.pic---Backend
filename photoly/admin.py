from django.contrib import admin
from .models import Photo, Comment, Rating

# Register your models here.
admin.site.register(Photo)
admin.site.register(Comment)
admin.site.register(Rating)
# admin.site.register(LikedPhoto)
