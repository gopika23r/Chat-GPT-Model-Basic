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
