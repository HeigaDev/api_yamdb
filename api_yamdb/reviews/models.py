from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Genre(models.Model):
    """Класс для описания жанров произведений"""
    name = models.CharField(
        'Название',
        max_length=256,
        help_text='Название жанра')
    slug = models.SlugField('Слаг жанра', max_length=50, unique=True)
    # description = models.TextField('Описание', null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Category(models.Model):
    """Класс для описания категорий произведений"""
    name = models.CharField(
        'Название',
        max_length=256,
        help_text='Название категории')
    slug = models.SlugField('Слаг категории', max_length=50, unique=True)
    # description = models.TextField('Описание', null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


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
        blank=True,
        null=True,
        related_name='reviews',
        verbose_name='Категория',
        help_text='Категория, к которой относится произведение'
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        null=True,
        related_name='reviews',
        verbose_name='Жанр',
        help_text='Жанр, к которому относится произведение'
    )
    """ through='GenreTitle', # on_delete=models.SET_NULL"""

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-year',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'


"""class GenreTitle(models.Model):
    # Класс для описания связи произведения и жанра
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'Жанр {self.title} - это {self.genre}'"""



"""author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
)"""