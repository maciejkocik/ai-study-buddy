import streamlit as st
from generator import generate_quiz_from_text

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