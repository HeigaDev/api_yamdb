from django.db import models

from reviews.validators import score_validate, year_validate
from user.models import User


class GenreCategoryModel(models.Model):
    """Абстрактная модель для жанров и категорий."""
    name = models.CharField(
        'Название',
        max_length=256)
    slug = models.SlugField('Индетификатор',
                            max_length=50,
                            unique=True,
                            db_index=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name


class ReviewCommentModel(models.Model):
    """Абстрактаная модель для создания комментариев и обзоров"""
    text = models.TextField(
        verbose_name='Текст',
        help_text='Текст публикации'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
        help_text='Дата устанавливается автоматически'
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.text


class Genre(GenreCategoryModel):
    """Класс для описания жанров произведений"""

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


Genre._meta.get_field('name').help_text = ('Название жанра')
Genre._meta.get_field('slug').help_text = ('Индетификатор жанра')


class Category(GenreCategoryModel):
    """Класс для описания категорий произведений"""

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
        validators=[year_validate],
        help_text='Год выпуска произведения')
    description = models.TextField(
        'Описание',
        help_text='Описание произведения')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория',
        help_text='Категория, к которой относится произведение'
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='Жанр',
        help_text='Жанр, к которому относится произведение'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-year',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'


class Review(ReviewCommentModel):
    """Модель отзывов"""
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Отзыв',
        help_text='Отзыв к выбранному произведению'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор отзыва',
    )
    score = models.PositiveSmallIntegerField(
        validators=[score_validate],
        verbose_name='Рейтинг',
        help_text='Рейтинг произведения'
    )

    class Meta:
        ordering = ('id',)
        constraints = (
            models.UniqueConstraint(
                fields=('title', 'author'),
                name='Unique_review_from_author_for_title'
            ),
        )
        verbose_name = 'Отзыв к произведению'
        verbose_name_plural = 'Отзывы к произведениям'


class Comment(ReviewCommentModel):
    """Модель комментариев"""
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментарий',
        help_text='Комментарий к отзыву'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Комментарий к отзыву'
        verbose_name_plural = 'Комментарии к отзывам'
