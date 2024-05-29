# WeatherApp-in-Django

WeatherApp is a simple web application built using Django that allows users to get the current weather information for any city in the world. It fetches data from a weather API and displays it in a user-friendly interface.

## Features

- Search for current weather by city name
- Display temperature, weather conditions, and other relevant data
- User-friendly interface

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/waqasbcs/weatherapp-in-django.git
   cd weatherapp-in-django

2. Create a virtual environment:
   python -m venv venv

3. Activate the virtual environment:
On Windows: venv\Scripts\activate
on mac or linux: source venv/bin/activate

4. Install the dependencies:
pip install -r requirements.txt

5. Set up your API key:
Obtain an API key from a weather service provider (e.g., OpenWeatherMap).
Create a .env file in the root directory and add your API key:
  WEATHER_API_KEY=your_api_key_here

6. Run the database migrations:
python manage.py migrate

7. Start the development server:
python manage.py runserver

8. Access the application:
Open your web browser and go to http://127.0.0.1:8000.

User
create a readme  file and also add scrrenshot "# Weatherapp-in-django" 
ChatGPT
Certainly! Below is a sample README file for a Django-based Weather App, along with instructions for adding a screenshot. You'll need to have a screenshot file ready, for example, screenshot.png.

README.md
markdown
Copy code
# WeatherApp-in-Django

WeatherApp is a simple web application built using Django that allows users to get the current weather information for any city in the world. It fetches data from a weather API and displays it in a user-friendly interface.

## Features

- Search for current weather by city name
- Display temperature, weather conditions, and other relevant data
- User-friendly interface

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/weatherapp-in-django.git
   cd weatherapp-in-django
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS and Linux:

bash
Copy code
source venv/bin/activate
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Set up your API key:

Obtain an API key from a weather service provider (e.g., OpenWeatherMap).

Create a .env file in the root directory and add your API key:

plaintext
Copy code
WEATHER_API_KEY=your_api_key_here
Run the database migrations:

bash
Copy code
python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver
Access the application:

Open your web browser and go to http://127.0.0.1:8000.

Usage
Enter the name of the city in the search box.
Click on the "Get Weather" button.
View the current weather information for the specified city.




























   


