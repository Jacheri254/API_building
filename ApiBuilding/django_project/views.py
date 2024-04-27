
import requests
from django.shortcuts import render 
from django.urls import path
from . import views

def index(request):
    response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    data = response.json()
    fact = data['text']

    r3 = requests.get('https://dog.ceo/api/breeds/image/random')
    res3 = r3.json()
    dog = res3['message']

    response2 = requests.get('https://freetestapi.com/api/v1/students')
    data2 = response2.json()
    name = data2[0]['name']

    response3 = requests.get('https://freetestapi.com/api/v1/movies?limit=5') 
    data3 = response3.json()
    movie = data3[0]['title']

    response4 = requests.get('https://freetestapi.com/api/v1/weathers/1')
    data4 = response4.json()
    weather = data4.get('weather_description')

    response5 = requests.get('https://freetestapi.com/api/v1/cars/1')
    data5 = response5.json()
    car = { 
         'id': data5.get('id', None),
          'make': data5.get('make', None),
        'model': data5.get('model', None),
        'year': data5.get('year', None),
        'color': data5.get('color', None),
        'mileage': data5.get('mileage', None),
        'price': data5.get('price', None),
        'fuelType': data5.get('fuelType', None),
        'transmission': data5.get('transmission', None),
        'engine': data5.get('engine', None),
        'horsepower': data5.get('horsepower', None),
        'features': data5.get('features', None),
        'owners': data5.get('owners', None)
       }
    
    return render(request, 'templates/index.html', {
        'fact': fact, 
        'dog': dog,  
        'name': name, 
        'movie': movie,
        'weather': weather, 
        'car': car
    })