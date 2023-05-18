import datetime as dt

from django.core.exceptions import ValidationError


def year_validate(value):
    current_year = dt.date.today().year
    if not (value <= current_year):
        raise ValidationError (
            ('Нельзя добавлять произведения, которые еще не вышли.'
            'Год выпуска не может быть больше текущего!')
        )

def score_validate(value):
    if not (0 < value < 11):
        raise ValidationError (
            'Вы можете поставить оценку от 1 до 10 баллов'
        )
    return value
