from django.contrib import admin
from BloggingApp.models import Category, Blog
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

# Custom Admin Columns

# Category
class CategoryAttributes(admin.ModelAdmin):
    list_display = ('cat_title', 'description', 'cat_URL', 'date_of_creation')
    search_fields = ('cat_title',)

# Blog
class BlogAttributes(admin.ModelAdmin):
    list_display = ('blog_title', 'category', 'blog_url', 'date_of_creation')
    search_fields = ('blog_title',)

    list_filter = ('category',)
    list_per_page = 10

class BlogCols(SummernoteModelAdmin, BlogAttributes):
    summernote_fields = ('blog_content',)


admin.site.register(Category, CategoryAttributes)
admin.site.register(Blog, BlogCols)



