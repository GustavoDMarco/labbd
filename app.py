import streamlit as st

st.title("Hello World!")


with st.form("Meu_form"):
    st.title("Cadastro Usuario:")
    nome = st.text_input("Nome: ")
    senha = st.text_input("Senha: ", type="password")
    st.selectbox("Escolha uma cidade", ['Rio Claro', "Sao Paulo"])
    submit = st.form_submit_button("Enviar")


st.write(nome)
