from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('donate/', views.donate, name='donate'),
]