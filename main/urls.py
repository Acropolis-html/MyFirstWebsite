from django.urls import path
from . import views
from .views import LoginUser
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.html),
    path('about', views.about),
    path('html', views.html, name='html'),
    path('test',views.test),
    path('buttons', views.buttons),
    path('login', views.LoginUser.as_view(), name='login'),
    path('register',views.RegisterUser.as_view(), name='register'),
    path('logout', views.LogoutUser, name='logout'),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='update_profile'),
]