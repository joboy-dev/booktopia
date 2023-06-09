from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('addBook/', views.AddNewBookView.as_view(), name='addBook'),
    path('bookDetail/<int:pk>/', views.BookDetailsView.as_view(), name='bookDetails'),
    path('allBooks/', views.AllBooksView.as_view(), name='allBooks'),
    path('authorBooks/', views.AuthorBooksView.as_view(), name='authorBooks'),
]