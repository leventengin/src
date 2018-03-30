from django.contrib import admin

from .models import BlogPost, MacPost

admin.site.register(BlogPost)
admin.site.register(MacPost)
