from django.contrib import admin
from .models import Post


# Register your models here.

admin.site.register(Post) #registered the model to make it visible on the admin page
