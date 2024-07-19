from django.urls import path

from gamestore import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.GameListView.as_view(), name='game-list'),
    path('games/<int:pk>/', views.GameDetailView.as_view(), name='game-detail'),
    path('games/add/', views.GameCreateView.as_view(), name='game-create'),
    path('games/<int:pk>/update/', views.GameUpdateView.as_view(), name='game-update'),
    path('games/<int:pk>/delete/', views.GameDeleteView.as_view(), name='game-delete'),
]
