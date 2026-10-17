"""Conversational Paris travel guide using the OpenAI Chat Completions API."""

from openai import OpenAI

MODEL = "gpt-4o-mini"

QUESTIONS = [
    "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?",
]


def main():
    """Ask three Paris travel questions while retaining conversation context."""
    client = OpenAI()  # Reads OPENAI_API_KEY from the environment.
    conversation = [
        {"role": "system", "content": "You are a helpful Paris travel guide."}
    ]

    for question in QUESTIONS:
        conversation.append({"role": "user", "content": question})

        response = client.chat.completions.create(
            model=MODEL,
            messages=conversation,
            temperature=0.0,
            max_tokens=100,
        )

        answer = response.choices[0].message.content or ""
        conversation.append({"role": "assistant", "content": answer})

        print(f"Question: {question}\nAnswer: {answer}\n")


if __name__ == "__main__":
    main()
