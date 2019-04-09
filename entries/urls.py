from django.urls import path
from . import views

urlpatterns = [
    path('inde/', views.index,name='inde'),
    
    path('add/', views.add, name='add'),
]
