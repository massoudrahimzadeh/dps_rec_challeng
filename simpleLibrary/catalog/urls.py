from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list' ),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/new/', views.BookCreateView.as_view(), name='book_create'),
    path('search/', views.SearchResultsView.as_view(), name='search'),
]
