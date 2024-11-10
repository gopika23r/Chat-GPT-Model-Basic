# Import necessary modules
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot("MyBot")

# Train the chatbot using the ChatterBot corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Function to interact with the chatbot
def chatbot_response(user_input):
    response = chatbot.get_response(user_input)
    return response

# Running the Chatbot
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
hasattr
import requests

def get_weather(city):
    api_key = "your_openweathermap_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data.get("main"):
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"The temperature in {city} is {temp}°C with {description}."
    else:
        return "City not found."

# Example interaction
city = input("Enter a city: ")
print(get_weather(city))

