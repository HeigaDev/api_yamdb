import datetime as dt

from django.core.exceptions import ValidationError


def year_validate(value):
    current_year = dt.date.today().year
    if not (value <= current_year):
        raise ValidationError(
            ('Нельзя добавлять произведения, которые еще не вышли.'
             'Год выпуска не может быть больше текущего!')
        )


def score_validate(value):
    if not (0 < value < 11):
        raise ValidationError(
            'Вы можете поставить оценку от 1 до 10 баллов'
        )
    return value


def email_validate(value):
    if not (0 < len(value) <= 254):
        raise ValidationError(
            'Содержимое поля email не должно быть длиннее 254 символа'
        )
    return value


def username_validate(value):
    if not (0 < len(value) <= 150):
        raise ValidationError(
            'Содержимое поля username не должно быть длиннее 150 символов'
        )
    return value