from django.contrib import admin

from .models import Category, Language, Artist, Song
# # Register your models here.

admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Artist)
admin.site.register(Song)
