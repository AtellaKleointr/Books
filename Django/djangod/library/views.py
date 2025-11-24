from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from .models import Book, User
from .forms import BookForm, UserForm


class HomeView(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'books'
    ordering = ['-created_at']


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'


class StatisticsView(TemplateView):
    template_name = 'statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.all()
        context['total_books'] = books.count()
        context['read_books'] = books.filter(status='read').count()
        context['reading_books'] = books.filter(status='reading').count()
        context['planned_books'] = books.filter(status='planned').count()
        context['postponed_books'] = books.filter(status='postponed').count()
        return context


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})