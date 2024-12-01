# AI Agent Project

## Overview

Welcome to the **AI Agent Project**. This project aims to create an interactive, evolving AI assistant capable of understanding user inputs, maintaining a memory of past interactions, and providing helpful responses using cutting-edge natural language processing technologies. The assistant will leverage the capabilities of the OpenAI API and aims to develop into a personalized, context-aware agent that can grow alongside its user.

The project is in an early stage but demonstrates a lot of promise in creating personalized AI agents that can learn, remember, and adapt to individual users. The ultimate vision is to develop an agent that truly understands the user’s needs, preferences, and previous conversations, enabling more meaningful and helpful interactions.

## Current Progress

- **Environment Setup**: Successfully created a Python virtual environment (`agent_env_3_10`) using Python 3.10 installed via Homebrew. This ensures an isolated workspace for our project dependencies.
- **OpenAI Integration**: Connected to OpenAI's API to leverage the latest language models. Integrated secure API key management using environment variables to ensure sensitive information is not stored directly in the codebase.
- **Chat Script Development**: Developed a script (`chat_with_openai.py`) that takes user input and interacts with OpenAI's GPT-4 model to generate responses. Tested and successfully retrieved responses, confirming that the integration is functional.
- **Project Structure**: Organized project files into logical folders for better maintainability. For example, moved scripts and memory files into the `src` directory for a cleaner structure.
- **Persistent Memory**: Added features to save interactions to persistent memory. This will help the agent remember previous conversations, providing continuity and improved response relevance.

## Vision

Our vision for this project is to create a **replicant AI** that remembers everything about its user, forming a personalized and evolving AI companion. Our long-term goals include:

1. **Memory**: Developing sophisticated, context-rich memory capabilities that allow the agent to learn from each interaction and adapt over time.
2. **Advanced NLP Features**: Integrating a variety of NLP models and services (like OpenAI) to provide the best responses based on user needs. Eventually, we'll explore tools beyond simple chat interactions, including action-taking capabilities.
3. **Integration of Tools**: Our future roadmap includes adding various tools that the AI can use autonomously, such as search functions, scheduling tasks, or even generating code.
4. **User-Centric Growth**: A key principle of this AI agent is to grow in tandem with its user. Every conversation will deepen the AI's understanding of the user’s preferences, resulting in a truly personalized experience.

## Getting Started

### Prerequisites
- Python 3.10 (installed via Homebrew)
- Virtual environment (`venv`) installed and activated
- `pip` for package management

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai_agent_project.git
   cd ai_agent_project

Set up the virtual environment:
```
python3 -m venv agent_env_3_10
source agent_env_3_10/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Configuration
Set up the OpenAI API key in your environment:
```
export OPENAI_API_KEY="your_openai_api_key_here"
```
This API key is used to authenticate with the OpenAI API and should not be committed to the repository.

Usage  
To run the chatbot script:
```
python src/scripts/chat_with_openai.py
```
This script will prompt you for input and generate a response from the AI.

Roadmap
Implement Archival Memory for long-term context management.
Develop Tool Usage capabilities, enabling the agent to use APIs and execute tasks autonomously.
Introduce User Profiles for multi-user support, with personalized experiences.
Contributing
We welcome contributions! Please create a pull request if you want to add new features or fix issues. Make sure to follow the existing coding style and add meaningful commit messages.

License
This project is licensed under the MIT License. See LICENSE for more information.

Contact
For more details, please reach out to Andres Carrillo or create an issue in this repository.
