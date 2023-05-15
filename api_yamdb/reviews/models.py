from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class GenreCategoryModel(models.Model):
    """Абстрактная модель. Добавляет дату создания."""
    name = models.CharField(
        'Название',
        max_length=256)
    slug = models.SlugField('Индетификатор', max_length=50, unique=True)

    class Meta:
        abstract = True


class Genre(GenreCategoryModel):
    """Класс для описания жанров произведений"""

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

Genre._meta.get_field('name').help_text = ('Название жанра')
Genre._meta.get_field('slug').help_text = ('Индетификатор жанра')


class Category(GenreCategoryModel):
    """Класс для описания категорий произведений"""

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

Category._meta.get_field('name').help_text = ('Название категории')
Category._meta.get_field('slug').help_text = ('Индетификатор категории')


class Title(models.Model):
    """Класс для описания произведений"""
    name = models.CharField(
        'Название',
        max_length=256,
        help_text='Название произведения')
    year = models.IntegerField(
        'Год выпуска',
        help_text='Год выпуска произведения')
    description = models.TextField(
        'Описание',
        help_text='Описание произведения')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='reviews',
        verbose_name='Категория',
        help_text='Категория, к которой относится произведение'
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='reviews',
        verbose_name='Жанр',
        help_text='Жанр, к которому относится произведение'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-year',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
