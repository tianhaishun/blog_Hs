from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),
    path('experience/', views.experience, name='experience'),
    path('projects/', views.projects, name='projects'),
] 