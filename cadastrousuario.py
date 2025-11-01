import streamlit as st
import time

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Palmeiras_logo.svg/300px-Palmeiras_logo.svg.png", width = 150)

with st.sidebar:
    st.title("Escolha a cidade")
  

with st.spinner("Carregando"):
    time.sleep(2)

st.balloons()

def cadastro_usuario(nome,senha):
    return

def validar(nome,senha):
    if nome=="" or senha=="":
        return False
    return True


with st.form("Cadastro Usuario"):
    st.title("Cadastro Usuario:")
    nome = st.text_input("Nome: ")
    senha = st.text_input("Senha: ", type="password")
    st.selectbox("Escolha uma cidade", ['Rio Claro', "Sao Paulo"])
    submit = st.form_submit_button("Enviar")


if submit and validar(nome, senha):
    cadastro_usuario(nome,senha)
    st.success("Cadastro com sucesso")
elif submit: 
    st.warning("Dados Inválidos")

st.write(st.secrets["db_username"])