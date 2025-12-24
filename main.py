from data_manager import get_quiz_list, load_quiz
from quiz_logic import check_answer, calculate_percentage
def main():
    
    print("--- ROZPOCZYNAM TESTOWANIE QUIZU (TRYB KONSOLI) ---")

    # 1. Wczytanie danych i ustawienie zmiennych

    quiz_list = get_quiz_list()

    print ("Wczytuję quiz:", quiz_list[0], "\n")

    questions = load_quiz(quiz_list[0])

    score = 0
    total_questions = len(questions)
    
    # 3. Główna pętla quizu (Main Loop)
    for i, q in enumerate(questions):
        print(f"\nPYTANIE {i+1}/{total_questions}:")
        print(q["pytanie"])  
        print("-" * 20)
        
        # Wyświetlanie opcji (Display options)
        options = q["opcje"]
        for key, text in options.items():
            print(f"{key.upper()}) {text}")
            
        # 4. Pobranie odpowiedzi od użytkownika (Get Input)
        user_choice = input("\nTwój wybór (a/b/c/d): ")
        
        # 5. Sprawdzenie logiki (Check Logic)
        is_correct = check_answer(user_choice, q["poprawna"])
        
        if is_correct:
            print("✅ DOBRZE!")
            score += 1
        else:
            print(f"❌ ŹLE! Poprawna odpowiedź to: {q['poprawna'].upper()}")
            
        # Wyświetlenie wyjaśnienia, jeśli istnieje w JSON
        explanation = q.get("wyjasnienie")
        if explanation:
            print(f"💡 INFO: {explanation}")

    # 6. Podsumowanie (Summary)
    percentage = calculate_percentage(score, total_questions)
    
    print("\n" + "=" * 30)
    print(f"KONIEC TESTU")
    print(f"Twój wynik: {score}/{total_questions} ({percentage:.0f}%)")
    print("=" * 30)

if __name__ == "__main__":
    main()