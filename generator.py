import os
import json
from google import genai
import config_secrets

# Inicjalizacja klienta (używamy klucza z config_secrets)
client = genai.Client(api_key=config_secrets.GOOGLE_API_KEY)

def generate_quiz_from_text(notes_text):
    """
    Wysyła tekst do Gemini i zwraca listę pytań w formacie JSON (lista słowników).
    """
    prompt = """
    Jesteś nauczycielem. Na podstawie poniższego tekstu stwórz 5 pytań quizowych.
    Zwróć TYLKO czysty kod JSON w formacie:
    [
        {
            "pytanie": "Treść pytania?",
            "opcje": { "a": "Opcja 1", "b": "Opcja 2", "c": "Opcja 3", "d": "Opcja 4" },
            "poprawna": "a", 
            "wyjasnienie": "Krótkie wyjaśnienie."
        }
    ]
    Nie używaj markdowna (```json).
    TEKST:
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt + notes_text
        )
        
        # Czyszczenie odpowiedzi (na wypadek gdyby model dodał ```json)
        text = response.text.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.endswith("```"):
            text = text[:-3]
            
        return json.loads(text)
    except Exception as e:
        print(f"Błąd generowania: {e}")
        return []