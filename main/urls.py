from django.urls import include, path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('robots.txt', TemplateView.as_view(template_name="main/robots.txt", content_type="text/plain"), name="robots_file"),	path('sitemap.xml', TemplateView.as_view(template_name="main/sitemap.xml", content_type="text/xml"), name="sitemap_file"),
    path('projects/', views.projects, name="projects"),
    path('resume/', views.resume, name="resume"),
    path('blog/', views.blog, name="blog"),
    path('blog/<post_id>/', views.blog_single, name="blog_post"),
    path('videos/', views.videos, name="videos"),
    path('add/video/', views.add_video, name="add_video"),
    path('edit/video/<video_id>/', views.edit_video, name="edit_video"),
    path('remove/video/<video_id>/', views.delete_video, name="delete_video"),
    path('add/blog', views.add_blog, name="add_blog"),
    path('remove/blog/<post_id>/', views.delete_blog, name="delete_blog"),
    path('edit/blog/<post_id>/', views.edit_blog, name="edit_blog"),
    path('add/project/', views.add_project, name="add_project"),
    path('edit/project/<project_id>/', views.edit_project, name="edit_project"),
    path('remove/project/<project_id>/', views.delete_project, name="delete_project"),
    path('edit/home/', views.edit_about, name="edit_about"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
