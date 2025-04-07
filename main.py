from faster_whisper import WhisperModel
from pydub import AudioSegment
import requests
import os
from dotenv import load_dotenv

load_dotenv()

name_file = "video.mp4"
file_location = f"/app/{name_file}"
type_file = name_file.split(".")[1]


audio_file = AudioSegment.from_file(file_location, format=type_file)
audio_file.export("/app/audio.mp3", format="mp3")

model = WhisperModel("medium", compute_type="int8")

segments, _ = model.transcribe("/app/audio.mp3", language="pt")

translated = " ".join([segment.text for segment in segments])


def improve_text_translated(text):
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    body = {
        "model": "qwen-2.5-32b",
        "messages": [
            {
                "role": "system",
                "content": (
                    "Você é um especialista em revisão de texto em português. "
                    "Sua tarefa é corrigir erros gramaticais, traduzir palavras que estiverem em inglês, "
                    "e deixar o texto natural, como se tivesse sido escrito por um falante nativo do português brasileiro. "
                    "Se o texto parecer confuso ou fora de contexto, reescreva de forma mais clara e fluida."
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
    result = response.json()
    return result["choices"][0]["message"]["content"]


print("Texto original transcrito:")
print(translated)

print("-------")

print("\nTexto após melhoria com Groq:")
print(improve_text_translated(translated))
