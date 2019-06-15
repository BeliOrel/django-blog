from django.contrib import admin
from .models import Post

# Register model Post -> to be accessible in the admin page
admin.site.register(Post)
