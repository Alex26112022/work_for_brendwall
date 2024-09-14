from django.core.exceptions import ValidationError


def validate_min_value(value):
    if value < 0:
        raise ValidationError('Значение должно быть больше нуля!')
