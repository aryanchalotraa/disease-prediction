def predict_disease_risk(weather, pm25):
    temperature = weather["temperature"]
    humidity = weather["humidity"]
    rainfall = weather["rainfall"]

    # Pollution-based airborne risk
    if pm25 > 60:
        return "High Airborne Disease Risk (Severe Pollution)"

    # Weather-based airborne risk
    if humidity > 70 and temperature > 28:
        return "High Airborne Disease Risk"

    # Waterborne disease risk
    if rainfall > 5:
        return "High Waterborne Disease Risk"

    return "Low Disease Risk"
