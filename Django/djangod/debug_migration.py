import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangod.settings')
django.setup()

from library.models import Book


def add_test_images():
    # Создаем простые тестовые изображения
    books = Book.objects.all()

    for book in books:
        if not book.cover_image:
            print(f"📖 Книга без обложки: {book.title}")

    print("\n💡 Добавьте книги через форму на сайте с изображениями!")


if __name__ == "__main__":
    add_test_images()