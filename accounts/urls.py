from django.urls import path
from . import views

urlpatterns = [
    path('',views.home ,name='home'),
    path('register/',views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('playlists/',views.playlists, name='playlists'),
    path('playlist/create/',views.create_playlist, name='create_playlist'),
    path('playlist/update/<int:playlist_id>/',views.update_playlist, name='update_playlist'),
    path('playlist/delete/<int:playlist_id>/',views.delete_playlist, name='delete_playlist'),
    path('search/',views.search, name='search'),
]
