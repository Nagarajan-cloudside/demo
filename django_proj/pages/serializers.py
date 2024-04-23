from rest_framework import serializers
from .models import Book

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        # table_name = "custom table name"
        table_name = 'books'
        fields = '__all__'
