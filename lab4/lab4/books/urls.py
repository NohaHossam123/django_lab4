from django.urls import path
from .views import display_books ,get_book , books_author
# , get_book

urlpatterns = [
    path('lists/', display_books),
    path('book/<int:id>', get_book, name = "book"),
    path('author/<id>' , books_author , name='author')
]