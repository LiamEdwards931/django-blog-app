from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
   
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_filter = ('approved', 'created_on')
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    search_fields = ['name', 'email_address', 'body']
    actions = ['approve_comments']

    def approve_comments(self, reuqest, queryset):
        queryset.update(approved=True)
