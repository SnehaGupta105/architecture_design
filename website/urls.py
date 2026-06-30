from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('features/', views.features, name='features'),
    path('2d-plans/', views.twodplans, name='twodplans'),
    path('3d-elevation/', views.threedelevation, name='threedelevation'),
    path('interior-design/', views.interiordesign, name='interiordesign'),
    path('consultation/', views.consultation, name='consultation'), 
    path('pricing/', views.pricing, name='pricing'),
    path('kitchen/', views.kitchen, name='kitchen'),
    path('bathroom/', views.bathroom, name='bathroom'),
    path('living-room/', views.livingroom, name='livingroom'),
    path('about/', views.about, name='about'),
    path('view_design/', views.view_design, name='view_design'),
]