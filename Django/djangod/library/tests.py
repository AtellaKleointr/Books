from django.test import TestCase
from django.urls import reverse
from .models import User, Book

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(
            name="Тестовый пользователь",
            email="test@example.com"
        )
        self.assertEqual(str(user), "Тестовый пользователь (test@example.com)")

class BookModelTest(TestCase):
    def test_book_creation(self):
        book = Book.objects.create(
            title="Тестовая книга",
            author="Тестовый автор",
            year=2024,
            genre="Тестовый жанр",
            annotation="Тестовая аннотация",
            status="planned"
        )
        self.assertEqual(str(book), "Тестовая книга - Тестовый автор")