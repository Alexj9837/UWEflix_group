from django.db import models
from UWEflix.models.clubs import Club
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
from django import forms
import uuid, re, datetime
from datetime import date, timedelta
    
class User(models.Model):
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

    # Representitive Info
    affiliatedClub = models.ForeignKey(Club, on_delete=models.CASCADE)
    #studentRepresentitive = models.ForeignKey(User, on_delete=models.CASCADE) # The rep must have an existing acc

    # Personal Info
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    DateOfBirth = models.DateField()

    def encryptPassword(self, plainPassword):
        self.password = make_password(plainPassword)

    def checkPassword(self, plainPassword):
        if check_password(plainPassword):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.affiliatedClub.clubName} Representitive"

class MonthAgoManager(models.Manager):
    def get_queryset(self):
        today = date.today()
        monthAgo = today - timedelta(days=30)
        return super().get_queryset().filter(date__gte=monthAgo, date__lte=today)

class UserPurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    totalCost = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField() # Will only ever store purcahses made on the day therefore needs to filter between month old purchases and beyond
    objects = MonthAgoManager()

    def __str__(self):
        return f"{self.user.firstName} {self.user.lastName} spent £{self.totalCost} on {self.quantity} tickets"
    
class ClubPurchaseHistory(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=10)
    totalCost = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField() # Will only ever store purcahses made on the day therefore needs to filter between month old purchases and beyond
    objects = MonthAgoManager()

    def __str__(self):
        return f"{self.club.clubName} club spent £{self.totalCost} on {self.quantity} tickets"