from django.shortcuts import render
from django.contrib import messages
import requests
import datetime


def index(request):
    city = request.POST['city'] if 'city' in request.POST else 'Lahore'
    OPENWEATHERMAP_API_KEY = '8f26bd76ad0ecd67f0aeb796c2722806'
    SEARCH_ENGINE_ID = '722a9bb9cb4364809'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}'
    PARAMS = {'units': 'metric'}

    GOOGLE_CUSTOM_SEARCH_API_KEY = 'AIzaSyDwGjaeynj9YdFnQGYAVxc92KyLziiLa8M'
    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={GOOGLE_CUSTOM_SEARCH_API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    image_url = 'https://example.com/default_image.jpg'
    if 'items' in data:
        search_items = data.get("items")
        if search_items:
            image_url = search_items[0]['link']

    try:
        data = requests.get(url, params=PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(request, 'weather/index.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city, 'exception_occurred': False, 'image_url': image_url})

    except KeyError:
        exception_occurred = True
        messages.error(request, 'Entered data is not available from the API')
        day = datetime.date.today()

        return render(request, 'weather/index.html', {'description': 'clear sky', 'icon': '01d', 'temp': 25, 'day': day, 'city': 'Lahore', 'exception_occurred': exception_occurred, 'image_url': image_url})
