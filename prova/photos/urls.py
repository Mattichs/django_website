from django.urls import path
from . import views

urlpatterns = [
    #path('', views.gallery, name='gallery'),
    #path('photo/<str:pk>/', views.viewPhoto, name='photo'),

    # UNI-ISOL path
    path('', views.homepage, name='homepage'),
    path('add/', views.add, name='add'),
    path('workDetail/<str:pk>/', views.workDetail, name='workDetail')
]
