from django.contrib import admin
from .models import userProfile

# Register your models here.
class userProfileAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'about')

admin.site.register(userProfile, userProfileAdmin)