from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']
