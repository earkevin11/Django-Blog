from django.contrib import admin

# Register your models here.
from .models import Post

#this registers our post model/class so that we can see/manage the posts in the admin page GUI.
admin.site.register(Post)