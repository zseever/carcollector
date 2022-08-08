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