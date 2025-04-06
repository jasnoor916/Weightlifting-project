from django.db import models
from django.db import models

class Sports(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Players(models.Model):
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sports, on_delete=models.CASCADE)

class Matches(models.Model):
    sport = models.ForeignKey(Sports, on_delete=models.CASCADE)
    date = models.DateField()
    venue = models.CharField(max_length=100)

class Bookings(models.Model):
    match = models.ForeignKey(Matches, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    booking_date = models.DateTimeField(auto_now_add=True)

# Create your models here.
