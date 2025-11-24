from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('statistics/', views.StatisticsView.as_view(), name='statistics'),
    path('add-user/', views.add_user, name='add_user'),
    path('add-book/', views.add_book, name='add_book'),
]