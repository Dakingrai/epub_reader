from django.shortcuts import render
from .models import Category, Book
import ebooklib
from ebooklib import epub

def home(request):
    category_list = Category.objects.all()

    args = {
        'categories': category_list,
    }
    return render(request, 'ereader/index.html', args)

def library_list(request, id):
    category_list = Category.objects.all()
    books = Book.objects.filter(category=id)
    genre_name = Category.objects.get(id=id)
    args = {
        'genre': genre_name,
        'books': books,
        'categories': category_list,
    }
    return render(request, 'ereader/library_list.html', args)

def readbook(request):
    book_id = request.GET.get('id')
    book = Book.objects.get(id=book_id)
    book_epub = epub.read_epub(book.book)
    chapters = []
    for item in book_epub.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_body_content().decode('utf-8'))
    args = {
        'chapters': chapters,
        'test': "<p>Hello</p>"
    }

    return render(request, 'book/book.html', args)





