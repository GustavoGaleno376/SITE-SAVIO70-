import streamlit as st

# Inicializando os feedbacks no session_state
if "feedbacks" not in st.session_state:
    st.session_state.feedbacks = []

# Função para mostrar o feedback existente
def show_feedbacks():
    if st.session_state.feedbacks:
        st.subheader("Feedbacks Anteriores:")
        for feedback in st.session_state.feedbacks:
            st.write(f"Classificação: {feedback['rating']} estrelas")
            st.write(f"Comentários: {feedback['comments']}")
            st.write(f"Data: {feedback['date']}")
            st.write("---")
    else:
        st.write("Nenhum feedback registrado ainda.")

# Título da página
st.title("Deixe seu Feedback")

# Exibição dos feedbacks existentes
show_feedbacks()

# Formulário para o feedback
st.subheader("Novo Feedback")

# Campo de classificação em estrelas (1 a 5)
rating = st.slider("Qual sua classificação para o sistema?", 1, 5, 3)

# Campo de comentários
comments = st.text_area("Deixe seu comentário sobre o sistema")

# Campo de data
from datetime import date
today = date.today()
feedback_date = today.strftime("%d/%m/%Y")

# Botão para enviar o feedback
if st.button("Enviar Feedback"):
    if comments:
        # Adicionando o feedback ao session_state
        st.session_state.feedbacks.append({"rating": rating, "comments": comments, "date": feedback_date})
        st.success("Obrigado pelo seu feedback!")
        # Limpa os campos após enviar
        st.experimental_rerun()
    else:
        st.warning("Por favor, insira um comentário.")
