from faster_whisper import WhisperModel
from pydub import AudioSegment
import requests
import os
from dotenv import load_dotenv

load_dotenv()

file_name = "video.mp4"
file_location = f"/app/{file_name}"
type_file = file_name.split(".")[1]


audio_file = AudioSegment.from_file(file_location, format=type_file)
audio_file.export("/app/audio.mp3", format="mp3")

model = WhisperModel("medium", compute_type="int8")

segments, _ = model.transcribe("/app/audio.mp3", language="pt")
segments_list = list(segments)


def format_srt_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:06.3f}".replace(".", ",")


def create_caption_srt(segments, file_name_caption="legendas.srt"):
    with open(file_name_caption, "w", encoding="utf-8") as file:
        for i, segment in enumerate(segments, 1):
            start = format_srt_time(segment.start)
            end = format_srt_time(segment.end)
            text = segment.text.strip()

            file.write(f"{i}\n")
            file.write(f"{start} --> {end}\n")
            file.write(f"{text}\n\n")


def improve_text(text):
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

    return response.json()["choices"][0]["message"]["content"]


caption_text = "\n".join(
    [
        f"{format_srt_time(s.start)} --> {format_srt_time(s.end)}\n{s.text}"
        for s in segments_list
    ]
)

improved_caption = improve_text(caption_text)

with open("/app/legendas.srt", "w", encoding="utf-8") as file:
    file.write(improved_caption)

print(f"- Foi gerado o arquivo legendas.srt")
