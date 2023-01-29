import time

def chat():
    print("Chatbot: Hello, I'm a chatbot. How can I help you today?\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "q", "exit"]:
            print("Chatbot: Goodbye! Have a great day.")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that. Could you repeat it?")

chat()
