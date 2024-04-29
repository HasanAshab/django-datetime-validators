from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def date_is_future_validator(value):
    message = _("Date must be in the future.")
    code = "date_is_future"
    if value <= timezone.now().date():
        raise ValidationError(message, code=code)


def date_is_present_or_future_validator(value):
    message = _("Date must be in the present or in the future.")
    code = "date_is_present_or_future"
    if value < timezone.now().date():
        raise ValidationError(message, code=code)


def date_is_past_validator(value):
    message = _("Date must be in the past.")
    code = "date_is_past"
    if value >= timezone.now().date():
        raise ValidationError(message, code=code)


def date_is_present_or_past_validator(value):
    message = _("Date must be in the present or in the past.")
    code = "date_is_present_or_past"
    if value > timezone.now().date():
        raise ValidationError(message, code=code)


def date_time_is_future_validator(value):
    message = _("Date must be in the future.")
    code = "date_is_future"
    if value <= timezone.now():
        raise ValidationError(message, code=code)


def date_time_is_present_or_future_validator(value):
    message = _("Date must be in the present or in the future.")
    code = "date_is_present_or_future"
    if value < timezone.now():
        raise ValidationError(message, code=code)


def date_time_is_past_validator(value):
    message = _("Date must be in the past.")
    code = "date_is_past"
    if value >= timezone.now():
        raise ValidationError(message, code=code)


def date_time_is_present_or_past_validator(value):
    message = _("Date must be in the present or in the past.")
    code = "date_is_present_or_past"
    if value > timezone.now():
        raise ValidationError(message, code=code)
