from weather_api import get_weather
from air_quality_api import get_aqi
from model import predict_disease_risk

CITY = "Delhi"

weather = get_weather(CITY)
pm25 = get_aqi(CITY)

# Fallback if API fails
if pm25 is None:
    pm25 = 150  # typical Delhi polluted value (for demo)

risk = predict_disease_risk(weather, pm25)

print("City:", CITY)
print("Temperature:", weather["temperature"], "°C")
print("Humidity:", weather["humidity"], "%")
print("Rainfall:", weather["rainfall"], "mm")
print("PM2.5:", pm25, "µg/m³")
print()
print("Disease Risk Prediction:", risk)
