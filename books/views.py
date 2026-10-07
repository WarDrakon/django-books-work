from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book

def product_list(request):
    books = Book.objects.all()
    return render(request, 'books/products.html', {'products': books})

def product_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        year = request.POST.get('year')
        genre = request.POST.get('genre')
        price = request.POST.get('price')

        if title and author and price:
            Book.objects.create(
                title=title, author=author, year=year, genre=genre, price=price
            )
            messages.success(request, f'Книгу "{title}" додано!')
            return redirect('product_list')

    return render(request, 'books/product_add.html')