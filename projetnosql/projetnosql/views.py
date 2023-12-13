from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            newBook = Book()
            newBook.title = form.cleaned_data.get('title')
            newBook.author = form.cleaned_data.get('author')
            newBook.content = form.cleaned_data.get('content')
            newBook.save(using='default')
            newBook.save(using='mongodb')
            # form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def book_list(request):
    booksPSQL = Book.objects.using('default')
    booksMongo = Book.objects.using('mongodb')
    return render(request, 'book_list.html', {'booksPSQL': booksPSQL, 'booksMongo': booksMongo})

def index(request):

    return HttpResponse("Accueil");