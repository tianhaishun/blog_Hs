from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),
    path('experience/', views.experience, name='experience'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.post_list, name='post_list'),
    path('blog/create/', views.post_create, name='post_create'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
    path('blog/<slug:slug>/edit/', views.post_update, name='post_update'),
    path('blog/<slug:slug>/delete/', views.post_delete, name='post_delete'),
    path('blog/<slug:slug>/comment/', views.comment_create, name='comment_create'),
] 