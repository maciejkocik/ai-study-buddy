def check_answer(user_answer, correct_answer):
    """
    Sprawdza, czy odpowiedź użytkownika zgadza się z poprawną.
    Ignoruje wielkość liter i białe znaki.
    """
    if not user_answer:
        return False
    # Porównujemy np. "a" z "A " -> po wyczyszczeniu "a" == "a"
    return user_answer.lower().strip() == correct_answer.lower().strip()

def calculate_percentage(score, total_questions):
    """
    Bezpiecznie oblicza wynik procentowy (zabezpieczenie przed dzieleniem przez 0).
    """
    if total_questions == 0:
        return 0
    return (score / total_questions) * 100