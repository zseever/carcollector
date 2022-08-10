from django.db import models
from django.urls import reverse

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.year} {self.make} {self.model}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id':self.id})

class Driver(models.Model):
    name = models.CharField(max_length=20)
    state = models.CharField(max_length=2)

    cars = models.ManyToManyField(Car)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('drivers_detail', kwargs={'pk': self.id})


class Review(models.Model):
    date = models.DateField()
    rating = models.IntegerField()
    desc = models.CharField(max_length=255)

    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.rating} on {self.date}'
    
