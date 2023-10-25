import requests
import os
from dotenv import load_dotenv


def get_data(city):
    
    load_dotenv()
    api_key = os.getenv('API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city.get()}&appid={api_key}'
    response = requests.get(url)
    responseData = None  # Setting a default value
    responseData = response.json()        
    return responseData
    
