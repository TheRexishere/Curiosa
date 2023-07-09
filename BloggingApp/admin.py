from django.contrib import admin
from BloggingApp.models import Category, Blog
# Register your models here.

# Custom Admin Columns

# Category
class CategoryAttributes(admin.ModelAdmin):
    list_display = ('cat_title', 'description', 'cat_URL', 'date_of_creation')
    search_fields = ('cat_title',)

# Blog
class BlogAttributes(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_content', 'category', 'blog_url', 'date_of_creation')
    search_fields = ('blog_title',)
    list_filter = ('category',)
    list_per_page = 10

admin.site.register(Category, CategoryAttributes)
admin.site.register(Blog, BlogAttributes)


