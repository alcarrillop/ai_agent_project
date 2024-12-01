import openai
import os

# Set the OpenAI API key from environment variable
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_openai(user_input):
    # Define the system prompt
    system_prompt = "You are a japanese hacker."

    # Use OpenAI's Chat API to get a response
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input},
        ]
    )

    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    user_input = input("You: ")
    response = chat_with_openai(user_input)
    print(f"AI: {response}")
