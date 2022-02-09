from django.db import models
from django.contrib.auth.models import AbstractUser


PERMISSION_CHOICES = (
    ("Admin", "Admin"),
    ("Sub Admin", "Sub Admin"),
    ("Customer", "Customer"),
    ("Staff", "Staff"),
)


class User(AbstractUser):
	user_status = models.CharField(
        max_length = 20,
        choices = PERMISSION_CHOICES,
        default = 'Customer'
        )
	first_name = models.CharField(
        max_length = 100,
        default = 'Customer'
        )
	last_name = models.CharField(
        max_length = 100,
        default = 'Customer'
        )