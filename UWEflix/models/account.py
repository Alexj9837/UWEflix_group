from django.db import models
from UWEflix.models.clubs import Club
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
from django import forms
import uuid, re, datetime
from datetime import date, timedelta
    
class Users(models.Model):
    # Identifiers
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    # Personal Info
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    dateOfBirth = models.DateField()

    def encryptPassword(self, plainPassword):
        self.password = make_password(plainPassword)

    def checkPassword(self, plainPassword):
        if check_password(plainPassword):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.username} ({self.firstName} {self.lastName})"


# Stores the account details for the club representitive
class Representitive(models.Model):
    # Identifiers
    password = models.CharField(max_length=255)

    # Personal Info
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    DateOfBirth = models.DateField()
    clubID = models.ForeignKey(Club, on_delete=models.CASCADE)

    def encryptPassword(self, plainPassword):
        self.password = make_password(plainPassword)

    def checkPassword(self, plainPassword):
        return check_password(plainPassword, self.password)

    def __str__(self):
        return f"{self.club.club_name} Representative"
    
class Account(models.Model):
    title = models.CharField(max_length=100)
    discount_rate = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=10)
    club = models.OneToOneField(Club, on_delete=models.CASCADE)