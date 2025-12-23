from data_manager import get_quiz_list, load_quiz

# Lista dostępnych quizów
quizy = get_quiz_list()
print("Dostępne quizy:", quizy)

# Wczytanie pierwszego quizu
quiz = load_quiz(quizy[0])

print(quiz["pytanie"])
for key, value in quiz["opcje"].items():
    print(f"{key}: {value}")

print("Poprawna odpowiedź:", quiz["poprawna"])
print("Wyjaśnienie:", quiz["wyjasnienie"])