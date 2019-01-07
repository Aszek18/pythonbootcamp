from django.shortcuts import render

# Create your views here.

import...
from books.views
def book_list(request):
    books = Book.objects.all()
    return