from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Book
from .forms import BookCreate
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    template_name = 'books/index.html'
    context_object_name = 'books_list'
    
    def get_queryset(self):
        return Book.objects.all()

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book-detail.html'

@csrf_exempt
def create(request):
    if request.method == 'POST':
        form = BookCreate(request.POST)
        form.save()
        return redirect('index')
        # if form.is_valid():
            
    form = BookCreate()

    return render(request,'books/create.html',{'form': form})

@csrf_exempt
def edit(request, pk, template_name='books/edit.html'):
    book = get_object_or_404(Book, pk=pk)
    form = BookCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

@csrf_exempt
def delete(request, pk, template_name='books/confirm_delete.html'):
    book = get_object_or_404(Book, pk=pk)
    if request.method=='POST':
        book.delete()
        return redirect('index')
    return render(request, template_name, {'object':book})

