from django.shortcuts import render

class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

cars = [
    Car('Honda', 'Accord', '2016'),
    Car('BMW','135i','2009'),
    Car('Tesla','Model 3','2022'),
    Car('Ford', 'Mustang','2019')
]


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    return render(request, 'cars/index.html', {
        'cars': cars,
    })