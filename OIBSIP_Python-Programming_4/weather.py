import requests

def get_weather(city_name):
    if not city_name:
        print("❌ Please enter a city name.")
        return

    city = get_city_data(city_name)
    
    if city is None:
        print("❌ City not found!")
        return

    weather = get_current_weather(city["latitude"], city["longitude"])
    if weather is None:
        print("Couldn't retrieve weather.")
        return

    display_city_info(city)
    display_weather(weather)

    return {
        "city": city,
        "weather": weather
    }



def get_city_data(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city,
        "count": 1
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        print("❌ Unable to connect to the weather service.")
        return None

    try:
        data = response.json()
    except ValueError:
        print("❌ Invalid response from server.")
        return None
        
    results = data.get("results")
    if not results:
        return None

    return results[0]



def get_current_weather(latitude, longitude):
    weather_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    try:
        weather_response = requests.get(weather_url, params=params, timeout=10)
        weather_response.raise_for_status()
    except requests.exceptions.RequestException:
        print("❌ Unable to connect to the weather service.")
        return None

    weather_data = weather_response.json()

    current = weather_data.get("current")
    if current is None:
        return None
    return current



def display_city_info(city):
    print("\n📍 Location Found!\n")
    print("━━━━━━━━━━ 📋 Details ━━━━━━━━━━\n")

    print(f"🏙️ City:         {city.get('name', 'Unknown')}")
    print(f"🌍 Country:      {city.get('country', 'Unknown')}")
    print(f"📌 Latitude:     {city.get('latitude', 'Unknown')}")
    print(f"📍 Longitude:    {city.get('longitude', 'Unknown')}")
    print(f"🕒 Timezone:     {city.get('timezone', "Unknown")}")
    print(f"👥 Population:   {city.get('population', 'Unknown')}")



def display_weather(weather):
    print("\n━━━━━━━━ 🌤️ Current Weather ━━━━━━━━\n")

    print(f"🌡️ Temperature:  {weather.get('temperature_2m', 'Unknown'):.1f} °C")
    print(f"💧 Humidity:     {weather.get('relative_humidity_2m', 'Unknown')}%")
    print(f"💨 Wind Speed:   {weather.get('wind_speed_10m', 'Unknown')} km/h")