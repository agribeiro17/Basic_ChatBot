import ollama

MODEL_NAME = "phi"

def chat_with_bot(prompt):
    """user sends a promt and chatbot will reply

    Args:
        prompt (_type_): User input
    """

    response = ollama.chat(
        model = MODEL_NAME,
        messages=[{"role", "user", "content", prompt}]
    )
    return response['message']['content']

if __name__ == "__main__":
    print("\n Hello Welcome to a Basic Chatbot!")
    print("If you would like to exit the chat with Ollama, please enter the following\n 'exit', 'quit', or 'bye' \n")

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break
        try:
            answer = chat_with_bot(user_input)
            print("ChatBot: ", answer)
        except Exception as e:
            print("Error", e)

