import json
import os

# Define the path to your memory file
MEMORY_FILE_PATH = 'src/memory/archival_memory.json'

# Load memory function
def load_memory():
    """Load memory from the specified JSON file."""
    if os.path.exists(MEMORY_FILE_PATH):
        with open(MEMORY_FILE_PATH, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []  # Return empty list if file is corrupt or empty
    return []

# Save memory function
def save_to_memory(new_entry):
    """Append a new memory entry to the specified JSON file."""
    memory = load_memory()
    memory.append(new_entry)
    with open(MEMORY_FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(memory, file, indent=4)

# Check if interaction already exists (useful for filtering duplicates)
def interaction_exists(memory, interaction):
    """Check if a specific interaction already exists in memory."""
    for record in memory:
        if record['interaction'] == interaction:
            return True
    return False

# Main Usage Example (Optional Testing)
if __name__ == '__main__':
    memory_data = load_memory()

    user_input_value = input("You: ")
    ai_response = "This is an AI-generated response."  # Placeholder for AI response

    # Add this interaction to memory
    if not interaction_exists(memory_data, user_input_value):
        save_to_memory({'interaction': user_input_value, 'response': ai_response})

    # Display the agent response
    print(f"Agent: {ai_response}")
