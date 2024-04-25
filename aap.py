from flask import Flask, render_template, request
import gpt_2_simple as gpt2
import random

app = Flask(__name__)

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

def greet_user():
    # Select a random greeting from the list
    greeting = random.choice(GREETINGS)
    return greeting

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_response = ""

        if user_input.lower() == "exit":
            bot_response = "Goodbye!"
        else:
            bot_response = generate_response("Question: " + user_input + "\nAnswer:")
        
        return render_template("index.html", bot_response=bot_response)

    return render_template("index.html", greeting=greet_user(), topics=TOPICS)

if __name__ == "__main__":
    app.run(debug=True)
