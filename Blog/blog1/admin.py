from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Tag
admin.site.register(Tag)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
admin.site.register(Post, PostAdmin)
