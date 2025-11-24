from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=100, verbose_name='Имя')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Book(models.Model):
    STATUS_CHOICES = [
        ('read', 'Прочитано'),
        ('reading', 'В процессе'),
        ('planned', 'Буду читать'),
        ('postponed', 'Отложено'),
    ]

    title = models.CharField(max_length=200, verbose_name='Название')
    author = models.CharField(max_length=100, verbose_name='Автор')
    year = models.IntegerField(verbose_name='Год издания')
    genre = models.CharField(max_length=100, verbose_name='Жанр')
    annotation = models.TextField(verbose_name='Аннотация')
    review = models.TextField(blank=True, verbose_name='Рецензия')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='planned',
        verbose_name='Статус'
    )
    cover_image = models.ImageField(
        upload_to='book_covers/',
        blank=True,
        null=True,
        verbose_name='Обложка книги'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.author}"

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'