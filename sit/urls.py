from django.urls import path

from . import views

urlpatterns = [
        
         path('', views.index, name='index'),
         path('accounts/sign/', views.register, name='sign'),
          path('accounts/logout/', views.logout1, name='logout'),

]