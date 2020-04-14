from django.shortcuts import render
from .models import Books
# Create your views here.

def display_books(request):
    books = Books.objects.all()
    context = {"books":books}
    return render(request, "books/showAllBooks.html", context) 
    

def get_book(request, id):
    book= Books.objects.get(pk=id)
    context={"book":book}
    return render (request, "books/getOneBook.html", context)


def books_author(request, id):
    books=  Books.objects.filter(author_id= id)
    context = {"books":books}
    return render (request, "books/authors.html", context)


