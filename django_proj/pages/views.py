from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets,  status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializers

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):


    def create(self, request):
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializers(queryset, many = True)
        return Response(serializer.data)
    
    
    def retrieve(self, request, pk=None):
        try:
            queryset = Book.objects.all()
            book = get_object_or_404(queryset, pk=pk)
            serializer = BookSerializers(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    

    def update(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializers(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
        except Book.DoesNotExist:
                        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response( status = status.HTTP_204_NO_CONTENT)
    