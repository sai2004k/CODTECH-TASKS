import nltk
import random
import re
import numpy as np

# Download NLTK resources
nltk.download('punkt')

# Define a simple set of responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Greetings!", "How can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "default": ["I'm sorry, I don't understand that.", "Can you rephrase that?", "I'm not sure how to respond to that."]
}

# Define a simple set of patterns
patterns = {
    r'hi|hello|hey': "greeting",
    r'bye|goodbye|see you': "goodbye",
    r'thank(s| you)?': "thanks"
}

def respond(user_input):
    # Normalize the input
    user_input = user_input.lower()
    
    # Check for patterns
    for pattern, response_type in patterns.items():
        if re.search(pattern, user_input):
            return random.choice(responses[response_type])
    
    return random.choice(responses["default"])

def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        response = respond(user_input)
        print(f"Chatbot: {response}")

if _name_ == "_main_":
    chatbot()