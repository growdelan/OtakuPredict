# OtakuPredict

Skrypt, który na podstawie przekazanych preferencji dotyczących anime:

- które lubimy,
- których nie lubimy,

ma za zadanie przewidzieć, które z przekazanych nowych anime będą nam się podobały i utworzyć spis w postaci pliku `recommended_anime.txt`.

## Jak to działa?

Skrypt dzięki wykorzystaniu few-shot learning analizuje przekazane przez nas przykłady anime i porównuje je z nowym tytułem i jego opisem. Jeśli uzna, że tytuł pasuje do naszych preferencji, dodaje go do pliku.

Jeśli któryś z tytułów podaliśmy jako ulubiony wraz z opisem, a dane anime ma kolejny sezon i nie ma opisu, model również je wybierze do polecanych.

## Uruchomienie

Instalujemy potrzebne paczki `pip3 install -r requirements.txt`

Model LLama3 8B jest używany za pośrednictwem [Groq](https://groq.com), dlatego wymagany jest klucz API, który można uzyskać [tutaj](https://console.groq.com/keys)

Aby skrypt działał poprawnie, należy wypełnić zawartość pliku `.env.example` oraz zmienić jego nazwę na `.env`
