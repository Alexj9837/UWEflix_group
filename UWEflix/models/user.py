from django.contrib.auth.models import AbstractUser
from django.db import models

class Custom_user(AbstractUser):
    role = models.CharField(max_length=50, choices=[
            ('Cinema manager', 'Cinema manager'),
            ('account manager', 'account manager'),
            ('club rep', 'club rep'),
            ('student', 'student')])