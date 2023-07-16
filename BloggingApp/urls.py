from django.urls import path
from BloggingApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="Home"),
    path('blog/<slug:blog_url>', views.show_blog, name="Blog"),
    path('category/<slug:cat_URL>', views.show_category, name="Category"),
    path('<int:page_num>', views.load_page, name='Blog Page Access'),
    path('category/<slug:cat_URL>/<int:page_num>', views.load_cat_page, name='Category Page Access'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

