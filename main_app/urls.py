from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='cars_index'),    
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name="cars_create"),
    path('cars/<int:car_id>/assoc_driver/<int:driver_id>/', views.assoc_driver, name='assoc_driver'),
    path('cars/<int:car_id>/unassoc_driver/<int:driver_id>/', views.unassoc_driver, name='unassoc_driver'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name="cars_update"),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name="cars_delete"),
    path('cars/<int:car_id>/add_review', views.add_review, name='add_review'),
    path('drivers/', views.DriverList.as_view(), name="driver_index"),
    path('drivers/create/', views.DriverCreate.as_view(), name="driver_create"),
]

