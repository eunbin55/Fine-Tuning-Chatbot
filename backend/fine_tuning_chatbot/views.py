from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import BookForm
from .models import Book
from .serializers import BookSerializer

@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
    

def book_list(request):
    books = Book.objects.all()
    return render(request, 'fine_tuning_chatbot/book_list.html', {'books': books})
