from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView, DetailView

from .models import Car, Driver, Review
from .forms import ReviewForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {
        'cars': cars,
    })

def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    drivers = car.driver_set.all().values_list('id')
    drivers_without = Driver.objects.exclude(id__in=drivers)
    reviews = car.review_set.all()
    review_form = ReviewForm()
    return render(request, 'cars/detail.html', {
        'car':car,
        'review_form':review_form,
        'drivers': drivers_without,
    })

class CarCreate(CreateView):
    model = Car
    fields = '__all__'

class CarUpdate(UpdateView):
    model = Car
    fields = '__all__'

class CarDelete(DeleteView):
    model = Car
    fields = '__all__'
    success_url = '/cars/'

def add_review(request, car_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.car_id = car_id
        new_review.save()
    return redirect('detail',car_id=car_id)

class DriverList(ListView):
    model = Driver
    fields = '__all__'

class DriverCreate(CreateView):
    model = Driver
    fields = '__all__'
    success_url = '/drivers/'

def assoc_driver(request, car_id, driver_id):
    car = Car.objects.get(id=car_id)
    car.driver_set.add(driver_id)
    return redirect('detail', car_id=car_id)


def unassoc_driver(request, car_id, driver_id):
    car = Car.objects.get(id=car_id)
    car.driver_set.remove(driver_id)
    return redirect('detail', car_id=car_id)