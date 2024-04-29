from django.core.exceptions import ValidationError
from django.test import SimpleTestCase
from django.utils import timezone
from myapp.validators import (
    date_is_future_validator,
    date_is_present_or_future_validator,
    date_is_past_validator,
    date_is_present_or_past_validator,
    date_time_is_future_validator,
    date_time_is_present_or_future_validator,
    date_time_is_past_validator,
    date_time_is_present_or_past_validator,
)


class ValidatorTestCase(SimpleTestCase):

    def test_date_is_future_validator(self):
        with self.assertRaises(ValidationError):
            date_is_future_validator(timezone.now())

    def test_date_is_present_or_future_validator(self):
        with self.assertRaises(ValidationError):
            date_is_present_or_future_validator(
                timezone.now() - timezone.timedelta(days=1)
            )

    def test_date_is_past_validator(self):
        with self.assertRaises(ValidationError):
            date_is_past_validator(timezone.now() + timezone.timedelta(days=1))

    def test_date_is_present_or_past_validator(self):
        with self.assertRaises(ValidationError):
            date_is_present_or_past_validator(
                timezone.now() + timezone.timedelta(days=1)
            )

    def test_date_time_is_future_validator(self):
        with self.assertRaises(ValidationError):
            date_time_is_future_validator(timezone.now())

    def test_date_time_is_present_or_future_validator(self):
        with self.assertRaises(ValidationError):
            date_time_is_present_or_future_validator(
                timezone.now() - timezone.timedelta(seconds=1)
            )

    def test_date_time_is_past_validator(self):
        with self.assertRaises(ValidationError):
            date_time_is_past_validator(timezone.now() + timezone.timedelta(seconds=1))

    def test_date_time_is_present_or_past_validator(self):
        with self.assertRaises(ValidationError):
            date_time_is_present_or_past_validator(
                timezone.now() + timezone.timedelta(seconds=1)
            )
