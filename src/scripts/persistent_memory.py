import json
import os

MEMORY_FILE_PATH = 'src/memory/archival_memory.json'

# Load memory function
def load_memory():
    """Load memory from the specified JSON file."""
    if os.path.exists(MEMORY_FILE_PATH):
        with open(MEMORY_FILE_PATH, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# Save memory function
def save_memory(memory):
    """Save the given memory to the specified JSON file."""
    with open(MEMORY_FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(memory, file, indent=4)

# Check if interaction already exists
def interaction_exists(memory, interaction):
    """Check if a specific interaction already exists in memory."""
    for record in memory:
        if record['interaction'] == interaction:
            return True
    return False

# Add to memory if not duplicate
def add_to_memory(memory, user_input, agent_response):
    """Add a new interaction to memory if it doesn't already exist."""
    if not interaction_exists(memory, user_input):
        memory.append({'interaction': user_input, 'response': agent_response})

# Main logic
if __name__ == '__main__':
    memory_data = load_memory()

    user_input_value = input("You: ")
    # Here is where you call your existing model to generate a response
    ai_response = "This is an AI generated response."  # Renamed variable

    # Add this interaction to memory if it's not already present
    add_to_memory(memory_data, user_input_value, ai_response)  # Updated variable name

    # Save updated memory to the file
    save_memory(memory_data)

    # Display agent response
    print(f"Agent: {ai_response}")  # Updated variable name