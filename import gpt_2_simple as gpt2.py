import gpt_2_simple as gpt2

# Download the GPT-2 model
gpt2.download_gpt2(model_name="124M")

# Start a TensorFlow session
sess = gpt2.start_tf_sess()

# Load the pre-trained GPT-2 model
gpt2.load_gpt2(sess)

def generate_response(prompt):
    # Generate a response from the GPT-2 model based on the prompt
    response = gpt2.generate(sess, prefix=prompt, return_as_list=True)[0]
    return response.strip()

def main():
    print("Welcome to the Climate Change Q&A Bot! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        prompt = "Question: " + user_input + "\nAnswer:"
        bot_response = generate_response(prompt)
        print("Bot:", bot_response)

if __name__ == "__main__":
    main()
