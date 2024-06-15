"""Funkcje dotyczące konfigurajic LLM"""

from groq import Groq

from llms import prompt


def groq_client(groq_api_key):
    """Inicjalizacja klienta Groq"""
    client = Groq(
        api_key=groq_api_key,
    )
    return client


def run_groq_model(groq_api_key: str, model: str, context: str) -> str:
    """Funkcja uruchamiająca dany model LLM"""
    client = groq_client(groq_api_key)
    chat_completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt.prompt(context)}],
        temperature=0.0,
        stream=False,
    )
    model_response = chat_completion.choices[0].message.content
    return model_response
