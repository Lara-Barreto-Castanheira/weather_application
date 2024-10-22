#Weather Application
#Importing the libraries
import requests
from rich import print
from datetime import datetime

#Displaying a Welcome message
def welcome_message():
  """Displays a Welcome message to the user"""
  print("[bold dark_turquoise]Welcome to the [u]Weather[/u]🤗 app![/bold dark_turquoise]")

#Displaying the credit to the app developer
def credit_developer():
  """Displays the credit to the developer who built the app"""
  print("[navajo_white1] - This app was created by [u]@Lara Castanheira[/u] - [/navajo_white1]")

#Display temperature
def display_temperature(day, temperature, unit='C'):
  """Displays a temperature with the day"""
  print(f"[bold hot_pink3]{day}[/bold hot_pink3]: {round(temperature)}º{unit}")

#Displaying the Current weather
def display_current_weather(city):
  """Displays the current weather"""
  api_key = "c94dbt7bba306fa243b9f337b604o509"
  api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"
  response = requests.get(api_url)
  current_weather_info = response.json()
  current_weather_city = current_weather_info["city"]
  current_weather_temperature = round(current_weather_info["temperature"]["current"])

  display_temperature("Today", round(current_weather_temperature))

#Displaying Forecast weather
def display_forecast_weather(city_name):
  """Displays the forecast weather"""
  api_key = "c94dbt7bba306fa243b9f337b604o509"
  api_url = f"https://api.shecodes.io/weather/v1/forecast?query={city_name}&key={api_key}"
  response = requests.get(api_url)
  forecast_weather_info = response.json()

  for day in forecast_weather_info["daily"]:
    timestamp = day["time"]
    date = datetime.fromtimestamp(timestamp)
    formatted_day = date.strftime("%A")
    temperature = day ["temperature"]["day"]

    if date.date() != datetime.today().date():
      display_temperature(formatted_day, round(temperature))


#Running the app
welcome_message()
city_name = input("Enter a city name: ").capitalize().strip()

if city_name:
  display_current_weather(city_name)
  print("\n[bold dark_turquoise]Forescast:[/bold dark_turquoise]")
  display_forecast_weather(city_name)
  print("\n\n")
  credit_developer()
else:
  print("[red]Please [bold]try again[/bold]![/red]😉")
  