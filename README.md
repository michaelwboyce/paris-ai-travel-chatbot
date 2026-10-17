# Paris AI Travel Chatbot

A simple conversational travel assistant for visitors to Paris, developed in Python with the OpenAI Chat Completions API.

## Project overview

This educational project demonstrates how to:
- Create a system instruction for a travel assistant.
- Organize chat messages as Python dictionaries in a list.
- Iterate over a list of tourist questions.
- Call the OpenAI Chat Completions API with `gpt-4o-mini`.
- Preserve both user and assistant messages for conversational context.

## Project files

- `paris_chatbot.py` — Main Python script
- `requirements.txt` — Python dependencies
- `.gitignore` — Files that should not be committed

## Getting started

**Prerequisites:** Python 3.9+ and an OpenAI API key. API usage may incur charges.

1. Clone this repository.
2. Install the dependency:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Set your API key as an environment variable. Do not commit it.

   **PowerShell (Windows):**
   ```powershell
   $env:OPENAI_API_KEY="your_api_key_here"
   ```

   **macOS/Linux:**
   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```

4. Run the program:

   ```bash
   python paris_chatbot.py
   ```

## How it works

The application starts with a system message that tells the model to act as a Paris travel guide. It then asks three questions about the Louvre, Eiffel Tower, and Arc de Triomphe. Each user message is appended to the conversation, sent to the model, and followed by the assistant response. This preserves context across calls.

Parameters `temperature=0.0` and `max_tokens=100` aim for more consistent, concise replies. Answers may still vary and can be incomplete or inaccurate; travel details should be verified with reliable sources.

## Skills demonstrated

Python lists and dictionaries · Iteration · OpenAI API integration · Prompt engineering · Conversation history

## Origin

Adapted from a completed DataCamp learning exercise, *Planning a Trip to Paris with the OpenAI API*. This is a learning/portfolio demonstration, not a production travel-planning system.
