from django.contrib import admin
from .models import Profile, Post ,LikePost


# Register your models here.

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ''
# admin.site.register(Profile,ProfileAdmin)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)