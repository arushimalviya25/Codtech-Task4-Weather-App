import requests

def get_weather(city_name, api_key):
    """Fetches real-time weather details using the OpenWeatherMap API."""
    # Base URL configuration for current weather queries
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Building out parameters for metric system (Celsius) and target city
    query_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(query_url)
        weather_data = response.json()
        
        # HTTP Status Code 200 means successful retrieval
        if weather_data.get("cod") == 200:
            main_stats = weather_data["main"]
            weather_desc = weather_data["weather"][0]["description"]
            wind_stats = weather_data["wind"]
            sys_stats = weather_data["sys"]
            
            print(f"\n==========================================")
            print(f" 📍 WEATHER REPORT: {weather_data['name']}, {sys_stats['country']}")
            print(f"==========================================")
            print(f" 🌡️  Current Temp : {main_stats['temp']}°C")
            print(f" 🤔  Feels Like   : {main_stats['feels_like']}°C")
            print(f" 💧  Humidity     : {main_stats['humidity']}%")
            print(f" 🌪️  Wind Speed   : {wind_stats['speed']} m/s")
            print(f" ☁️  Condition    : {weather_desc.capitalize()}")
            print(f"==========================================\n")
        else:
            print(f"\n❌ Error: City '{city_name}' not found. Please verify the spelling.")
            
    except requests.exceptions.RequestException:
        print("\n❌ Connectivity Error: Unable to access the weather matrix. Verify connection.")

def run_app():
    print("--- Welcome to your Weather Forecast Console ---")
    
    # ⚠️ PASTE YOUR COPIED OPENWEATHERMAP API KEY INSIDE THE QUOTES BELOW:
    API_KEY = "b8c6b35dd1e6f4d9520749f56f9e0024"
    
    if API_KEY == "YOUR_APT_KEY_HERE":
        print("\n[Setup Notice]: Please paste your OpenWeatherMap API key into the script code first!")
        return

    while True:
        city = input("Enter a city name to search (or type 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            print("Closing the weather station. Stay dry!")
            break
        if city == "":
            continue
        get_weather(city, API_KEY)

if __name__ == "__main__":
    run_app()
