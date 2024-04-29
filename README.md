# Django Date Validators

A set of custom validators for validating date and datetime fields for Django.

## Installation

1. Install the package using pip:

```bash
pip install django-datetime-validators
```

2. Add `datetime_validators` to `INSTALLED_APPS`
```python
INSTALLED_APPS = [
    ...,
    "datetime_validators",
]
```
## Usage

### Date Is Future Validator

Checks if a date is in the future.

```python
from datetime_validators.validators import date_time_is_future_validator

# Using in Models
due_date = models.DateTimeField(
    validators=[date_time_is_future_validator]
)

```

### Other Validators

- **date_is_future_validator**: Checks if a date is in the future.
- **date_is_present_or_future_validator**: Ensures that a date is either in the present or in the future.
- **date_is_past_validator**: Validates that a date is in the past.
- **date_is_present_or_past_validator**: Checks if a date is either in the present or in the past.
- **date_time_is_future_validator**: Validates if a datetime is in the future.
- **date_time_is_present_or_future_validator**: Checks if a datetime is either in the present or in the future.
- **date_time_is_past_validator**: Ensures that a datetime is in the past.
- **date_time_is_present_or_past_validator**: Validates that a datetime is either in the present or in the past.


# Contributing
Contributions are more than wellcome :)