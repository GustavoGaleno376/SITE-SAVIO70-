import streamlit as st

# Inicializando a variável no session_state, se ainda não existir
if "usu_reserv" not in st.session_state:
    st.session_state["usu_reserv"] = {"nome": "", "email": "", "senha": ""}

# Página de Cadastro
st.title("Cadastro de Usuário")

# Campos de entrada para o cadastro
nome = st.text_input("Nome:", value=st.session_state["usu_reserv"]["nome"])
email = st.text_input("Email:", value=st.session_state["usu_reserv"]["email"])
senha = st.text_input("Senha:", type="password", value=st.session_state["usu_reserv"]["senha"])

if st.button("Cadastrar"):
    if len(nome) < 4:
        st.warning("O nome deve ter pelo menos 4 caracteres.")
    elif len(email) < 6:
        st.warning("Digite um email válido.")
    elif len(senha) < 7:
        st.warning("A senha deve ter pelo menos 7 caracteres.")
    else:
        # Salvar as credenciais no session_state
        st.session_state["usu_reserv"] = {"nome": nome, "email": email, "senha": senha}
        st.success(f"Bem-vindo(a), {nome}! Seu cadastro foi realizado com sucesso.")
