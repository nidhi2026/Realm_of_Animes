from django.urls import path
from . import views 

urlpatterns = [
    path('', views.trending, name="trending"),
    path('anime/<int:anime_id>/', views.get_anime, name='get_anime'),
    path('manga/<int:manga_id>/', views.get_manga, name='get_manga'),
    path('anime/genre/<str:genre>/', views.get_genre_anime, name='get_genre_anime'),
    path('manga/genre/<str:genre>/', views.get_genre_manga, name='get_genre_manga'),
    path('in_watchlater', views.in_watchlater, name="in_watchlater"),
    path('in_readlater', views.in_readlater, name="in_readlater"),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('readlist/', views.readlist, name='readlist'),
]
