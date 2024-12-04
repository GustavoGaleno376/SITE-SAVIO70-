import streamlit as st

# Garantir que as credenciais foram cadastradas
if "usu_reserv" not in st.session_state:
    st.session_state["usu_reserv"] = {"nome": "", "email": "", "senha": ""}

# Verificar se o usuário está cadastrado
if not all(st.session_state["usu_reserv"].values()):
    st.warning("Nenhum cadastro encontrado. Por favor, realize o cadastro antes de acessar seu perfil.")
    st.stop()  # Impede a execução do restante do código

# Página do Perfil
st.title("Meu Perfil")

st.subheader("Suas Informações")
st.write(f"**Nome:** {st.session_state['usu_reserv']['nome']}")
st.write(f"**Email:** {st.session_state['usu_reserv']['email']}")

# Opção para atualizar os dados
st.subheader("Atualizar Dados")
novo_nome = st.text_input("Atualize seu Nome:", value=st.session_state["usu_reserv"]["nome"])
novo_email = st.text_input("Atualize seu Email:", value=st.session_state["usu_reserv"]["email"])

if st.button("Salvar Alterações"):
    st.session_state["usu_reserv"]["nome"] = novo_nome
    st.session_state["usu_reserv"]["email"] = novo_email
    st.success("Seus dados foram atualizados com sucesso!")

# Botão para redefinir o cadastro
if st.button("Redefinir Cadastro"):
    st.session_state["usu_reserv"] = {"nome": "", "email": "", "senha": ""}
    st.success("Seu cadastro foi redefinido. Por favor, faça o cadastro novamente.")
