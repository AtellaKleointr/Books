from django import forms
from .models import Book, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите ваше имя'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Введите ваш email'
            }),
        }
        labels = {
            'name': 'Имя',
            'email': 'Email адрес',
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'genre', 'annotation', 'review', 'status', 'cover_image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Название книги'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Автор книги'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Год издания'
            }),
            'genre': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Жанр'
            }),
            'annotation': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Аннотация книги',
                'rows': 4
            }),
            'review': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Ваша рецензия',
                'rows': 4
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'cover_image': forms.FileInput(attrs={
                'class': 'form-input',
                'accept': 'image/*'
            })
        }
        labels = {
            'title': 'Название книги',
            'author': 'Автор',
            'year': 'Год издания',
            'genre': 'Жанр',
            'annotation': 'Аннотация',
            'review': 'Ваша рецензия',
            'status': 'Статус чтения',
            'cover_image': 'Обложка книги',
        }