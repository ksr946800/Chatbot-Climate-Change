import tkinter as tk
from tkinter import scrolledtext, messagebox
import gpt_2_simple as gpt2
import random

# Download the GPT-2 model
gpt2.download_gpt2(model_name="124M")

# Start a TensorFlow session
sess = gpt2.start_tf_sess()

# Load the pre-trained GPT-2 model
gpt2.load_gpt2(sess)

# Greetings to enhance interactivity
GREETINGS = [
    "Hello!",
    "Hi there!",
    "Welcome!",
    "Greetings!",
    "Nice to see you!",
    "Hey!",
]

# Predefined topics for buttons
TOPICS = [
    "Climate Change",
    "Renewable Energy",
    "Environmental Conservation",
    "Global Warming",
    "Sustainable Development",
]

def generate_response(prompt):
    # Generate a response from the GPT-2 model based on the prompt
    response = gpt2.generate(sess, prefix=prompt, return_as_list=True)[0]
    return response.strip()

def send_message(user_input):
    user_input = user_input.strip()
    
    if not user_input:
        return
    
    chat_area.insert(tk.END, "You: " + user_input + "\n")
    
    if user_input.lower() == 'exit':
        chat_area.insert(tk.END, "Bot: Goodbye!\n")
        chat_area.yview(tk.END)
        return
    
    if "climate change" in user_input.lower():
        # Add specific response to climate change-related queries
        prompt = "Question: " + user_input + "\nAnswer:"
        bot_response = generate_response(prompt)
    else:
        # Generate a generic response
        bot_response = generate_response("Question: " + user_input + "\nAnswer:")
    
    chat_area.insert(tk.END, "Bot: " + bot_response + "\n")
    chat_area.yview(tk.END)

def greet_user():
    # Select a random greeting from the list
    greeting = random.choice(GREETINGS)
    chat_area.insert(tk.END, "Bot: " + greeting + "\n")
    chat_area.yview(tk.END)

def clear_chat():
    # Clear the chat history
    chat_area.delete(1.0, tk.END)

def topic_button_clicked(topic):
    # Handler for topic buttons
    chat_area.insert(tk.END, "You: " + topic + "\n")
    send_message(topic)

# Create the main window
root = tk.Tk()
root.title("Climate Change Q&A Bot")

# Create a text area for displaying the chat history
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
chat_area.pack(padx=10, pady=10)

# Create predefined topic buttons
topic_frame = tk.Frame(root)
topic_frame.pack(pady=(0, 10))

for topic in TOPICS:
    topic_button = tk.Button(topic_frame, text=topic, command=lambda t=topic: topic_button_clicked(t))
    topic_button.pack(side=tk.LEFT, padx=5)

# Create an entry field for user input
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=(0, 10))

# Create a button to send messages
send_button = tk.Button(root, text="Send", command=lambda: send_message(entry.get()))
send_button.pack(side=tk.LEFT, padx=(10, 5))

# Create a button to clear the chat history
clear_button = tk.Button(root, text="Clear Chat", command=clear_chat)
clear_button.pack(side=tk.LEFT, padx=(0, 10))

# Greet the user when the application starts
greet_user()

root.mainloop()