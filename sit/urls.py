from django.urls import path
from . import views

urlpatterns = [
        
         path('', views.index, name='index'),
         path('sit/index1/', views.index1, name='index1'),
         path('accounts/sign/', views.register, name='sign'),
         path('accounts/logout/', views.logout1, name='logout'),
         path('coll/', views.coll, name='coll'),
         path('indo/', views.indo, name='indo'),
        

]