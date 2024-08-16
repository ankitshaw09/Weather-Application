import requests
from django.shortcuts import render
from .models import CitySearch

def index(request):
    if request.method == "POST":
        city = request.POST['city']
        weather_data = get_weather_data(city)
        if weather_data:
            CitySearch.objects.create(city=city, temperature=weather_data['temperature'])
        return render(request, 'weather/index.html', {
            'weather_data': weather_data,
            'history': CitySearch.objects.all().order_by('-search_date')
        })

    return render(request, 'weather/index.html', {
        'history': CitySearch.objects.all().order_by('-search_date')
    })

def get_weather_data(city):
    url = f"http://wttr.in/{city}?format=%C+%t+%w"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text.split()
        return {
            'condition': data[0],
            'temperature': data[1],
            'wind': data[2]
        }
    return None
