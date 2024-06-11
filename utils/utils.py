"""Funkcje zawierające operacje na plikach"""

import requests  # type: ignore


def load_prompt(filename):
    """Funkcja do wczytywania promptu system_prompt.txt"""
    with open(filename, "r", encoding="utf-8") as file:
        prompt = file.read()
    return prompt


def save_to_file(data, file_name):
    """Funkcja do zapisywania rekomendowanych anime"""
    with open(file_name, "w", encoding="utf-8") as file:
        for item in data:
            file.write(item + "\n")


def fetch_data(url, page=1):
    """Funkcja do pobrania zawartości wyniku API"""
    response = requests.get(url, params={"page": page})
    if response.status_code == 200:
        return response.json()
    raise requests.HTTPError(
        f"Błąd pobierania danych z interfejsu API: {response.status_code}"
    )
