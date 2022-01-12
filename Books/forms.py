from django import forms
from .models import Book

class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'title',
            'author',
            'publication_date',
            'gender',
            'isbn',
        )