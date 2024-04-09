from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

#from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    #fields = ("title", )
    list_display = ("title","author", "counted_view","login_require", "status", "published_date", "created_date")
    list_filter = ('status',"author")
    #ordering = ('-created_date',)
    search_fields = ('title', 'content')
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    #fields = ("title", )
    list_display = ("name", "post",  "approved", "created_date")
    list_filter = ('approved','post')
    #ordering = ('-created_date',)
    search_fields = ('name', 'post')
    


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)