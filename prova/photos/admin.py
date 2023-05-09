from django.contrib import admin

# Register your models here.

from .models import Photo, Category, Work, Image

admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Work)
admin.site.register(Image)