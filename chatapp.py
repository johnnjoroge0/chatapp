import time

def chat():
    print("Chatbot: Hello, I'm a chatbot. How can I help you today?\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I help you today?")
        elif user_input.lower() in ["how are you", "how are you doing"]:
            print("Chatbot: I'm doing well, thank you for asking! How about you?")
        elif user_input.lower() in ["what's your name", "what is your name"]:
            print("Chatbot: My name is Chatbot, nice to meet you!")
        elif user_input.lower() in ["quit", "q", "exit"]:
            print("Chatbot: Goodbye! Have a great day.")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that. Could you repeat it?")

chat()