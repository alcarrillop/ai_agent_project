import json
import os

# Define the memory file path
MEMORY_FILE = "../memory/archival_memory.json"

# Function to save memory to a JSON file
def save_to_memory(data):
    # Check if memory file exists; if not, create it
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as file:
            json.dump([], file)
    
    # Load existing memory
    with open(MEMORY_FILE, "r") as file:
        memory = json.load(file)
    
    # Add new data and save it back
    memory.append(data)
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)

# Test the function by saving some dummy data
if __name__ == "__main__":
    test_data = {
        "interaction": "First test interaction",
        "response": "This is a response to the first test"
    }
    save_to_memory(test_data)
    print(f"Data saved to memory: {test_data}")
