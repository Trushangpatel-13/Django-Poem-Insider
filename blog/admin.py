from django.contrib import admin
from .models import Post,CategoryList,Profile,Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(CategoryList)
admin.site.register(Profile)
admin.site.register(Comment)

