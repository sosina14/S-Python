import requests

API_KEY = '617464791b944aeb818183229242509'  # Your actual API key
city = "Addis Abeba"  # Your city
url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # Extract relevant weather information
        temperature = data['current']['temp_c']
        weather_description = data['current']['condition']['text']
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather_description}")
    else:
        print("Error fetching weather data. Please check the API key or city name.")
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
