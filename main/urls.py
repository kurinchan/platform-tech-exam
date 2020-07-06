from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('blog/', views.blog, name='blog'),
    path('blog/<str:pk>/update', views.update_blog, name='update_blog'),
    path('blog/<str:pk>/delete', views.delete_blog, name='delete_blog'),

    path('code/', views.code, name='code'),
    path('code/<str:pk>/', views.view_code, name='view_code'),
    path('code/<str:pk>/update', views.update_code, name='update_code'),
    path('code/<str:pk>/delete', views.delete_code, name='delete_code'),

    path('portfolio/', views.portfolio, name='portfolio'),

]
