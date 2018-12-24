from django.contrib import admin
from .models import Post, Comment, Favorite


class PostAdmin(admin.ModelAdmin):

    list_display = ('id', 'author', 'title', 'favorite_num', 'created_date', 'published_date')


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'author', 'title', 'created_date', 'published_date')


admin.site.register(Post, PostAdmin)

admin.site.register(Comment)
admin.site.register(Favorite)


