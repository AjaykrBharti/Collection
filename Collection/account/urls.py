from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import index,update,delete

urlpatterns = [
    path('',index,name='accounts' ),
    path('account/update/<str:pk>/',update,name='account/update'),
    path('account/delete/<str:pk>/',delete,name='account/delete'),

]