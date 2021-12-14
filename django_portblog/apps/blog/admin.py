from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Category, Comment

# Register your models here.
#admin.site.register(Post)
#admin.site.register(Category)

class PostsAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'img')
    search_fields=('title', 'author', 'created_on')
    list_per_page=25

    readonly_fields=['post_image']

    def post_image(self, obj):
        return mark_safe(
            '<a href="{0}"><img src="{0}" width="20%"></a>'.format(self.image.url)
        )

admin.site.register(Post, PostsAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(Category, CategoryAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'comment_body', 'post_id', 'created_on', 'approved_comment')
    list_filter = ('approved_comment', 'created_on')
    search_fields = ('author','comment_body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved_comment=True)

admin.site.register(Comment, CommentAdmin)