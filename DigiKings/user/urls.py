
from django import urls
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout', logout, name='logout'),
    path('404', Error404, name = 'Error404'),

    path('profile/', profile, name='profile'),

    # path('updateProfile/' , updateProfile , name = 'updateProfile'),

    path('token/', token_send, name='token_send'),
    path('verify/<str:auth_token>', verify_token, name='verify_token'),
    path('Profile/completed',Profile_Completed,name="Profile_Completed"),
    # Admin Panel
    path('admin-panel/', adminPanelHome, name='adminPanelHome'),

]
