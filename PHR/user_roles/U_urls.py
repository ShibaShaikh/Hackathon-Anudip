from django.urls import path
from . import views

urlpatterns = [
    # my Added routes
    path('', views.home_view, name='home'),
    #path('login/', views.login_view, name='login'),
    #path('register/', views.register_view, name='register'),
    #path('logout/', views.logout_view, name='logout'),
    #path('profile/', views.profile_view, name='profile'),
]
