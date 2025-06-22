import requests
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')

#  Your OpenWeather API key here
API_KEY = "946c0ef719f7d8cf084bce4e9df8e390"

#  Extract city name from user message
def extract_city(text):
    tokens = word_tokenize(text.lower())
    for i, word in enumerate(tokens):
        if word in ['in', 'at', 'for'] and i + 1 < len(tokens):
            return tokens[i + 1].capitalize()
    return None

#  Get weather from OpenWeather API
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200 or data.get("cod") != 200:
            return "I couldn't find the weather for that city."

        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        return f"The weather in {city} is {description} with {temp}°C and {humidity}% humidity."

    except Exception as e:
        return f"Something went wrong: {str(e)}"

#  Chatbot interaction loop
def chat():
    print("WeatherBot: Ask me about the weather (e.g., 'What’s the weather in Mumbai?'). Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("WeatherBot: Stay safe! ☀️")
            break
        city = extract_city(user_input)
        if city:
            print("WeatherBot:", get_weather(city))
        else:
            print("WeatherBot: Please mention a city (e.g., 'in Mumbai').")

#  Run the chatbot
if __name__ == "__main__":
    chat()
