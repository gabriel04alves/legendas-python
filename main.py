import streamlit as st
from ui.app import app

st.set_page_config(
    page_title="LegendaIA",
    page_icon="🎤",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("Gerador de Legendas")

input_type = st.radio("Escolha o tipo de input:", ("URL do vídeo", "Upload de vídeo"))

uploaded_video = (
    st.text_input("Digite a URL do vídeo:")
    if input_type == "URL do vídeo"
    else st.file_uploader("Faça upload de um vídeo", type=["mp4"])
)

if uploaded_video:
    app(uploaded_video)

    # with tempfile.TemporaryDirectory() as temp_dir:
    #     sanitized_name = re.sub(r"[^\w\-_.]", "_", uploaded_video.name)
    #     input_video_path = os.path.join(temp_dir, sanitized_name)
    #     extracted_audio_path = os.path.join(temp_dir, "audio.mp3")
    #     output_srt_path = os.path.join(temp_dir, "legendas.srt")
    #     output_video_path = os.path.join(temp_dir, f"{sanitized_name}_com_legenda.mp4")

    #     with open(input_video_path, "wb") as f:
    #         f.write(uploaded_video.read())

    #     st.write("Extraindo áudio...")
    #     extract_audio(input_video_path, extracted_audio_path)

    #     st.write("Transcrevendo áudio...")
    #     segments = list(transcribe_audio(extracted_audio_path))

    #     st.write("Melhorando o texto das legendas...")
    #     for segment in segments:
    #         segment["text"] = improve_text(segment["text"])

    #     st.write("Criando arquivo SRT...")
    #     create_srt(segments, output_srt_path)

    #     st.write("Aplicando legendas ao vídeo...")
    #     apply_subtitle(input_video_path, output_srt_path, output_video_path)

    #     st.success("Legendas geradas e aplicadas com sucesso!")

    #     with open(output_video_path, "rb") as f:
    #         video_bytes = f.read()
    #         st.download_button(
    #             label="Download do vídeo",
    #             data=video_bytes,
    #             file_name=f"{sanitized_name}_com_legenda.mp4",
    #             mime="video/mp4",
    #         )

    #     st.write("Assista o conteúdo gerado:")
    #     st.video(output_video_path)
