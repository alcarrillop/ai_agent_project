import openai
import os
from persistent_memory import save_to_memory, load_memory
import signal
import sys

# Set the OpenAI API key from environment variable
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# To keep track of the conversation
conversation_memory = []

# Function to handle SIGINT (e.g., ctrl + C) for clean exit
def exit_gracefully(sig, frame):
    """Handler to save memory and exit gracefully when interrupted."""
    print("\nSaving conversation memory...")
    for interaction in conversation_memory:
        save_to_memory(interaction)
    print("Memory saved. Exiting now.")
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, exit_gracefully)

def chat_with_openai(user_input, memory_context):
    # Define the system prompt
    system_prompt = "You are a sweet women from Colombia with a good sense of humor."

    # Construct messages list based on memory context and current user input
    messages = [{"role": "system", "content": system_prompt}]
    
    # Add memory context (previous interactions)
    for interaction in memory_context:
        messages.append({"role": "user", "content": interaction['interaction']})
        messages.append({"role": "assistant", "content": interaction['response']})
    
    # Add the current user input as the latest message
    messages.append({"role": "user", "content": user_input})

    # Use OpenAI's Chat API to get a response
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )

    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    # Load existing memory
    memory = load_memory()

    try:
        while True:
            # Get user input
            user_input = input("You: ")

            # Generate response using OpenAI API, incorporating memory context
            ai_response = chat_with_openai(user_input, memory)

            # Display response
            print(f"AI: {ai_response}")

            # Save the interaction to in-memory list (for saving later)
            conversation_memory.append({
                "interaction": user_input,
                "response": ai_response
            })

    except KeyboardInterrupt:
        # Trigger the graceful exit on CTRL+C
        exit_gracefully(None, None)
