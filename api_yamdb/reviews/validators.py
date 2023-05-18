import datetime as dt

from django.core.exceptions import ValidationError


def score_validate(value):
    if not (0 < value < 11):
        raise ValidationError(
            'Вы можете поставить оценку от 1 до 10 баллов'
        )
    return value
