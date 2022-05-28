import requests


api_key = "b6347d13b01b282fea0f722412236519"

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat=34.0522&lon=-118.2437&exclude=current, minutely, daily,alerts&appid={api_key}")
response.raise_for_status()