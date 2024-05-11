# models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Cinema(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    opening_hours = models.CharField(max_length=255)
    halls = models.ManyToManyField('CinemaHall')

class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField()

class Session(models.Model):
    cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE)
    movie = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=5, decimal_places=2)
    available_seats = models.IntegerField()

class Ticket(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    seat_number = models.IntegerField()