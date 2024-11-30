class ActiveMemory:
    def __init__(self, max_capacity=5):
        # Initialize with a maximum capacity for short-term memory
        self.max_capacity = max_capacity
        self.memory = []

    def add_interaction(self, interaction):
        # Add a new interaction to active memory
        if len(self.memory) >= self.max_capacity:
            # Remove the oldest interaction if memory exceeds capacity
            self.memory.pop(0)
        self.memory.append(interaction)

    def get_memory(self):
        # Return all interactions currently in active memory
        return self.memory

# Test the ActiveMemory class
if __name__ == "__main__":
    active_memory = ActiveMemory(max_capacity=3)

    # Adding some test interactions
    active_memory.add_interaction("First interaction")
    active_memory.add_interaction("Second interaction")
    active_memory.add_interaction("Third interaction")
    active_memory.add_interaction("Fourth interaction")  # This will push out the first one

    # Print out current active memory
    print("Active Memory:", active_memory.get_memory())
