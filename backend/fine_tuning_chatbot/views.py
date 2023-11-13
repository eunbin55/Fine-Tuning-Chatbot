from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'fine_tuning_chatbot/create_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'fine_tuning_chatbot/book_list.html', {'books': books})
