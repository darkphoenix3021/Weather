import requests
import sys

def get_weather(city_name, api_key):
    """Fetches and displays weather data from OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request ('metric' gets temperature in Celsius)
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric' 
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() # Raise an exception for bad status codes
        
        weather_data = response.json()
        
        # Extracting specific data from the JSON response
        city = weather_data['name']
        country = weather_data['sys']['country']
        description = weather_data['weather'][0]['description'].capitalize()
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        
        # Displaying the results beautifully in the terminal
        print("\n" + "="*45)
        print(f" 🌍 Weather in {city}, {country}")
        print("="*45)
        print(f" 🌥️  Condition   : {description}")
        print(f" 🌡️  Temperature : {temp}°C (Feels like {feels_like}°C)")
        print(f" 💧 Humidity    : {humidity}%")
        print(f" 💨 Wind Speed  : {wind_speed} m/s")
        print("="*45 + "\n")
        
    except requests.exceptions.HTTPError:
        if response.status_code == 401:
            print("\n❌ Error: Invalid API Key. Please check your OpenWeatherMap API key.")
        elif response.status_code == 404:
            print(f"\n❌ Error: City '{city_name}' not found. Please check the spelling.")
        else:
            print(f"\n❌ HTTP error occurred: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Failed to connect. Please check your internet connection.")
    except Exception as err:
        print(f"\n❌ An unexpected error occurred: {err}")


if __name__ == "__main__":
    print("🌤️  Welcome to the CLI Weather App!")
    
    # ⚠️ IMPORTANT: Replace the string below with your actual API key
    API_KEY = "YOUR_API_KEY_HERE"
    
    if API_KEY == "YOUR_API_KEY_HERE":
         print("\n[!] Setup Required:")
         print("    You need an OpenWeatherMap API key for this app to work.")
         print("    1. Go to https://openweathermap.org/api")
         print("    2. Sign up for a free account and generate an API Key.")
         print("    3. Paste your key into the 'API_KEY' variable in the script.\n")
         
    while True:
        city_input = input("Enter city name (or type 'quit' to exit): ").strip()
        
        if city_input.lower() == 'quit':
            print("\nGoodbye! Stay safe in the weather! ⛅\n")
            sys.exit()
            
        if city_input:
            get_weather(city_input, API_KEY)
        else:
            print("Please enter a valid city name.")
