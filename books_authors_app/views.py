from django.shortcuts import render, redirect	# notice the import!
from .models import Book, Author
def index(request):
    return redirect("/books")

def authors(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, "authors.html", context)

def add_author(request):
    Author.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'])
    return redirect("/authors")

def view_author(request,id):
    current_author = Author.objects.get(id = id)
    context = {
        "author": Author.objects.get(id = id),
        "books": Book.objects.exclude(authors = current_author)
    }
    return render(request, "view-author.html",context)

def add_author_to_book(request):
    book = Book.objects.get(title = request.POST['book-title'])
    author = Author.objects.get(id = request.POST['author-id'])
    book.authors.add(author)
    return redirect(f"/authors/{request.POST['author-id']}")

def books(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, "books.html", context)

def add_book(request):
    Book.objects.create(title = request.POST['title'], description = request.POST['description'])
    return redirect("/books")

def view_book(request,id):
    current_book = Book.objects.get(id = id)
    context = {
        "book": Book.objects.get(id = id),
        "authors": Author.objects.exclude(books = current_book)
    }
    return render(request, "view-book.html", context)

def add_book_to_author(request):
    book = Book.objects.get(id = request.POST['book-id'])
    author = Author.objects.get(id = request.POST['author-id'])
    book.authors.add(author)

    return redirect(f"/books/{request.POST['book-id']}")

