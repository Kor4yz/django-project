from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('education/', views.education, name='education'),
    path('algorithm/', views.algorithm, name='algorithm'),
    path('gallery/', views.gallery, name='gallery'),
]
