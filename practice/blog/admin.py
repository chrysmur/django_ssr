from django.contrib import admin

# Register your models here. to appear in the admin page
from .models import Post

admin.site.register(Post)
