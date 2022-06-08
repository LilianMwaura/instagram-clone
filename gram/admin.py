from django.contrib import admin
from .models import *
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('categories',)
    
admin.site.register(Profile)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Image)