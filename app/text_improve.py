import streamlit as st
import os
import requests
from dotenv import load_dotenv

load_dotenv()


def improve_text(text):
    headers = {
        "Authorization": f"Bearer {os.environ['GROQ_API_KEY']}",
        "Content-Type": "application/json",
    }

    body = {
        "model": "qwen-2.5-32b",
        "messages": [
            {
                "role": "system",
                "content": (
                    "Você é um especialista em revisão de texto em português. "
                    "Sua tarefa é corrigir erros gramaticais e traduzir termos "
                    "Se o texto parecer confuso ou fora de contexto, reescreva de forma mais clara e fluida sem fugir do tom e do contexto dele."
                    "Caso existam gírias, adapte-as para termos amplamente compreendidos, mantendo a coerência com o estilo e o contexto do texto."
                    "Retorne apenas o conteúdo revisado, sem explicações ou comentários adicionais."
                ),
            },
            {
                "role": "user",
                "content": f"Corrija e melhore esse texto transcrito: {text}",
            },
        ],
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions", headers=headers, json=body
    )
    data = response.json()

    if "choices" in data and data["choices"]:
        return data["choices"][0]["message"]["content"]
    else:
        st.error(f"Erro na API Groq: {data}")
        raise RuntimeError(f"Erro na API Groq: {data}")
