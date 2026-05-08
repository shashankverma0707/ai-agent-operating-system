import ollama
from app.config.settings import OLLAMA_MODEL


def ask_llm(prompt: str):
    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]