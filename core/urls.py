from django.urls import path
from . import Controllers

urlpatterns = [
    path('', Controllers.index, name='index'),
    path('settings', Controllers.settings, name='settings'),
    path('upload', Controllers.upload, name='upload'),
    path('follow', Controllers.follow, name='follow'),
    path('search', Controllers.search, name='search'),
    path('profile/<str:pk>', Controllers.profile, name='profile'),
    path('like_post', Controllers.like_post, name='like_post'),
    path('signup', Controllers.signup, name='signup'),
    path('signin', Controllers.signin, name='signin'),
    path('logout', Controllers.logout, name='logout')
]
