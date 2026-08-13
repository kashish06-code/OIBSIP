from weather import get_weather

def main():
    print("=" * 40)
    print("🌤️  Weather App")
    print("=" * 40)

    city_name = input("\n🏙️ Enter city name: ").strip()
    
    weather_data = get_weather(city_name)
    return weather_data


if __name__ == "__main__":
    main()
