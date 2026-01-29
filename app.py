import streamlit as st
from generator import generate_quiz_from_text
from quiz_logic import check_answer, calculate_percentage

st.set_page_config(page_title="AI Study Buddy", page_icon="🎓")

st.title("🎓 AI Study Buddy")
st.write("Wklej swoje notatki, a sztuczna inteligencja przygotuje dla Ciebie quiz!")

# 1. Sekcja wprowadzania danych
notes = st.text_area("Twoje notatki:", height=200)

# Inicjalizacja stanu (żeby quiz nie znikał po kliknięciu)
if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = None

if st.button("Generuj Quiz 🚀"):
    if not notes:
        st.warning("Najpierw wklej notatki!")
    else:
        with st.spinner("AI analizuje tekst..."):
            # Wywołanie funkcji z generator.py
            quiz_data = generate_quiz_from_text(notes)
            if quiz_data:
                st.session_state.quiz_data = quiz_data
                st.success("Quiz gotowy! Rozwiąż go poniżej.")
            else:
                st.error("Wystąpił błąd podczas generowania quizu.")

# 2. Sekcja wyświetlania quizu
if st.session_state.quiz_data:
    st.markdown("---")
    st.subheader("📝 Twój Quiz")

    # Używamy formularza, żeby sprawdzić wszystkie odpowiedzi na raz
    with st.form("quiz_form"):
        user_answers = {}
        
        for i, q in enumerate(st.session_state.quiz_data):
            st.markdown(f"**Pytanie {i+1}:** {q['pytanie']}")
            
            # Przygotowanie opcji do wyświetlenia
            options_display = [f"{k}) {v}" for k, v in q['opcje'].items()]
            
            # Widget wyboru (Radio button)
            choice = st.radio(
                "Wybierz odpowiedź:",
                options_display,
                key=f"q_{i}",
                index=None # Domyślnie nic nie zaznaczone
            )
            
            # Zapisujemy tylko literkę (np. "a") do sprawdzenia
            if choice:
                user_answers[i] = choice.split(")")[0] # bierze "a" z "a) Treść"

        submitted = st.form_submit_button("Sprawdź wyniki")

    # 3. Sprawdzanie wyników po kliknięciu przycisku
    if submitted:
        score = 0
        total = len(st.session_state.quiz_data)
        
        for i, q in enumerate(st.session_state.quiz_data):
            user_choice = user_answers.get(i)
            correct_choice = q['poprawna']
            
            is_correct = check_answer(user_choice, correct_choice)
            
            if is_correct:
                st.success(f"Pytanie {i+1}: ✅ Dobrze!")
                score += 1
            else:
                st.error(f"Pytanie {i+1}: ❌ Źle. Poprawna to: {correct_choice}")
                st.info(f"Wyjaśnienie: {q['wyjasnienie']}")
        
        # Wyświetlanie wyniku końcowego
        percentage = calculate_percentage(score, total)
        if percentage >= 80:
            st.balloons() 
            st.success("🎉 REWELACJA! Jesteś mistrzem!")
        elif percentage >= 50:
            st.info("👍 Dobry wynik!")
        else:
            st.warning("💪 Jeszcze trochę nauki i będzie super!")

        st.metric(label="Twój Wynik", value=f"{percentage:.0f}%", delta=f"{score}/{total} pkt")