import os
import json

# Ścieżka do folderu z quizami
QUIZ_FOLDER = "quizy"

# Funkcja do pobierania listy plików quizów
def get_quiz_list():
    
    return [
        file
        for file in os.listdir(QUIZ_FOLDER)
        if file.endswith(".json")
    ]

# Funkcja do ładowania zawartości pliku quizu
def load_quiz(nazwa_pliku):
    path = os.path.join(QUIZ_FOLDER, nazwa_pliku)

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
