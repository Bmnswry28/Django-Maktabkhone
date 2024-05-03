from django.contrib import admin
from blog.models import Post
class postadmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    empty_value_display = '-empty-'
    list_display = ('title' ,'author','counted_views','status','published_date','created_date')
    search_fields = ['title','content','author']
admin.site.register(Post,postadmin)
