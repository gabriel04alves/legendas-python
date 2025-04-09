import streamlit as st
import re
import os
import tempfile
from app.audio_processing import extract_audio
from app.transcription import transcribe_audio
from app.text_improve import improve_text
from app.srt_create import create_srt
from app.apply_subtitle import apply_subtitle


def app(uploaded_video):
    with tempfile.TemporaryDirectory() as temp_dir:
        sanitized_name = re.sub(r"[^\w\-_.]", "_", uploaded_video.name)
        input_video_path = os.path.join(temp_dir, sanitized_name)
        extracted_audio_path = os.path.join(temp_dir, "audio.mp3")
        output_srt_path = os.path.join(temp_dir, "legendas.srt")
        output_video_path = os.path.join(temp_dir, f"{sanitized_name}_com_legenda.mp4")

        with open(input_video_path, "wb") as f:
            f.write(uploaded_video.read())

        st.write("Extraindo áudio...")
        extract_audio(input_video_path, extracted_audio_path)

        st.write("Transcrevendo áudio...")
        segments = list(transcribe_audio(extracted_audio_path))

        st.write("Melhorando o texto das legendas...")
        for segment in segments:
            segment["text"] = improve_text(segment["text"])

        st.write("Criando arquivo SRT...")
        create_srt(segments, output_srt_path)

        st.write("Aplicando legendas ao vídeo...")
        apply_subtitle(input_video_path, output_srt_path, output_video_path)

        st.success("Legendas geradas e aplicadas com sucesso!")

        with open(output_video_path, "rb") as f:
            video_bytes = f.read()
            st.download_button(
                label="Download do vídeo",
                data=video_bytes,
                file_name=f"{sanitized_name}_com_legenda.mp4",
                mime="video/mp4",
            )

        st.write("Assista o conteúdo gerado:")
        st.video(output_video_path)
