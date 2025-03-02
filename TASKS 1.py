import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Constants
API_KEY = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
CITY = 'London'  # Change to your desired city
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

# Fetch data from OpenWeatherMap
response = requests.get(URL)
data = response.json()

# Check if the request was successful
if response.status_code == 200:
    # Extract relevant data
    weather_data = {
        'City': data['name'],
        'Temperature (°C)': data['main']['temp'],
        'Humidity (%)': data['main']['humidity'],
        'Weather': data['weather'][0]['description']
    }
    
    # Create a DataFrame
    df = pd.DataFrame([weather_data])
    
    # Print the DataFrame
    print(df)

    # Visualization
    plt.figure(figsize=(10, 5))
    
    # Bar plot for temperature and humidity
    sns.barplot(data=df[['Temperature (°C)', 'Humidity (%)']])
    plt.title(f'Weather in {CITY}')
    plt.ylabel('Value')
    plt.xticks(ticks=[0, 1], labels=['Temperature (°C)', 'Humidity (%)'])
    plt.grid(axis='y')
    
    # Show the plot
    plt.show()
else:
    print(f"Error fetching data: {data['message']}")
