import streamlit as st
from ui.app import app

st.set_page_config(
    page_title="LegendaIA",
    page_icon="🎤",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("Gerador de Legendas")

input_type = st.radio(
    "Escolha o como enviar o vídeo:", ("URL do vídeo", "Upload de vídeo")
)

uploaded_video = (
    st.text_input("Digite a URL do vídeo:")
    if input_type == "URL do vídeo"
    else st.file_uploader("Faça upload de um vídeo", type=["mp4"])
)

if uploaded_video:
    app(uploaded_video)
