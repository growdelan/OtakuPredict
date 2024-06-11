"""Głowny plik skryptu"""

import os
from dotenv import load_dotenv

from llms import groq
from utils import utils


def main(url: str, model: str):
    """Głowna funkcja do predykcji Anime"""
    load_dotenv()
    system_prompt = utils.load_prompt("./system_prompt.txt")
    recommended_anime = []
    season_anime_data = utils.fetch_data(url)

    for anime in season_anime_data["data"]:
        response = groq.run_groq_model(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model=model,
            system_prompt=system_prompt,
            context=f"Title: {anime['title']}\nDescription: {anime['synopsis']}",
        )

        if response.lower() == "yes":
            recommended_anime.append(
                f"\nTitle: {anime['title']}\nDescription: {anime['synopsis']}\n\n"
                + "#" * 30
            )
            print(
                f"\nTitle: {anime['title']}\nDescription: {anime['synopsis']}\n\n"
                + "#" * 30
            )

    if recommended_anime:
        utils.save_to_file(recommended_anime, "./recommended_anime.txt")
    else:
        print("Brak rekomendacji w tym sezonie.")


if __name__ == "__main__":
    API_URL = "https://api.jikan.moe/v4/seasons/now"
    MODEL_NAME = "llama3-8b-8192"
    main(API_URL, MODEL_NAME)
