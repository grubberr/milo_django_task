
from __future__ import unicode_literals
import random
from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(default=date.today)
    random = models.IntegerField(
        default=lambda: random.randint(1, 100),
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ])
