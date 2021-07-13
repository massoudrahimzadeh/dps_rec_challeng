from django.shortcuts import render
from .forms import Book_input_form
from .models import Book
from django.views.generic import (CreateView, ListView, DetailView)
from django.db.models import Q

class BookListView(ListView):
    model= Book

    def get_queryset(self):
        return Book.objects.all().order_by('-title')

class BookDetailView(DetailView):
    model=Book

class BookCreateView(CreateView):
    model=Book
    redirect_field_name = 'catalog/book_detail.html'

    form_class = Book_input_form
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)

class SearchResultsView(ListView):
    model = Book
    template_name = 'search.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
        return object_list
