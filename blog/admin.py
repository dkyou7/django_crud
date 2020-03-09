from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','img','content']
    list_display_links=['id','title']
    list_filter = ['created','updated']
    list_editable = ['content']
    # list_per_page = 50
    # default : 100

# admin.site.register(Post)