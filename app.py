from data_manager import get_quiz_list, load_quiz

# Lista dostępnych quizów
quizy = get_quiz_list()
print("Dostępne quizy:", quizy, "\n")

# Wczytanie pierwszego quizu
quiz = load_quiz(quizy[0])
print ("Wczytuję quiz:", quizy[0], "\n")

# Wyświetlanie pytań
for q in quiz:
    print("Pytanie:", q["pytanie"])
    print("Poprawna odpowiedź:", q["poprawna"])
    print("Wyjaśnienie:", q["wyjasnienie"])
    print("\n")