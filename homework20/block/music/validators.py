from django.core.exceptions import ValidationError
import re

def validate_login(value):
    if not re.match(r'[0-9a-zA-Z]{6,10}$', value):
        raise ValidationError(
            ('Invalid value: %(value)s'),
            params = {'value': value},
        )

def validate_email(value):
    if not re.match(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", value):
        raise ValidationError(
            ('Invalid value %(value)s '),
            params={'value': value},
        )