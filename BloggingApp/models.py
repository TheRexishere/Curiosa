from django.db import models

# Create your models here.

# Categories
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    category_id = models.AutoField(primary_key=True)
    cat_title = models.CharField(max_length=100)
    description = models.TextField()
    cat_URL = models.CharField(max_length=100)
    cat_view_count = models.IntegerField(default=0)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_title
    

# Blog
class Blog(models.Model):

    class Meta:
        verbose_name_plural = 'Blogs'

    blog_id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=100)
    blog_content = models.TextField()
    blog_url = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    blog_image = models.ImageField(upload_to="blog_img/")
    blog_view_count = models.IntegerField(default=0)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.blog_id)
    
    
