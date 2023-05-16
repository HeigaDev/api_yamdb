import datetime as dt

from django.core.exceptions import ValidationError


def year_validate(value):
    current_year = dt.date.today().year
    if not (value <= current_year):
        raise ValidationError (
            ('Нельзя добавлять произведения, которые еще не вышли.'
            'Год выпуска не может быть больше текущего!')
        )
    return value