import json
import os
import sys
from google import genai

# --- KONFIGURACJA ---
INPUT_FILE = "notatki.txt"
OUTPUT_FOLDER = "quizy"
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "nowy_quiz.json")

try:
    import config_secrets
    api_key = config_secrets.GOOGLE_API_KEY
except (ImportError, AttributeError):
    print("❌ Błąd: Brak klucza w config_secrets.py")
    sys.exit(1)

client = genai.Client(api_key=api_key)
MODEL_ID = "gemini-flash-latest"

SYSTEM_PROMPT = """
Jesteś nauczycielem. Na podstawie tekstu stwórz 5 pytań quizowych ABCD.
Zwróć TYLKO czysty JSON jako listę:
[
  {
    "pytanie": "Treść?",
    "opcje": {"a": "...", "b": "...", "c": "...", "d": "..."},
    "poprawna": "a",
    "wyjasnienie": "Krótkie wyjaśnienie."
  }
]
"""

def generate_quiz():
    if not os.path.exists(INPUT_FILE):
        print(f"⚠️ Brak pliku {INPUT_FILE}")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        notes = f.read()

    print(f"🚀 Generowanie przy użyciu {MODEL_ID}...")
    
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=f"{SYSTEM_PROMPT}\n\nNOTATKI:\n{notes}"
    )

    quiz_data = parse_ai_response(response.text)

    if quiz_data:
        if not os.path.exists(OUTPUT_FOLDER):
            os.makedirs(OUTPUT_FOLDER)
            
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(quiz_data, f, indent=4, ensure_ascii=False)
        print(f"✅ Quiz zapisany w: {OUTPUT_FILE}")
    else:
        print("❌ Błąd: AI nie zwróciło poprawnego formatu JSON.")

def parse_ai_response(text):
    text = text.strip()
    if "```json" in text: text = text.split("```json")[1].split("```")[0]
    elif "```" in text: text = text.split("```")[1]
    try:
        return json.loads(text.strip())
    except:
        return None

if __name__ == "__main__":
    generate_quiz()