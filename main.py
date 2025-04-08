from app.audio_processing import extract_audio
from app.transcription import transcribe_audio
from app.text_improve import improve_text
from app.format_srt_time import format_srt_time
from app.srt_create import create_srt
from app.apply_subtitle import apply_subtitle

INPUT_VIDEO = "/app/video.mp4"
EXTRACTED_AUDIO = "/app/audio.mp3"
OUTPUT_SRT = "/app/legendas.srt"
OUTPUT_VIDEO = "/app/video_com_legenda.mp4"

extract_audio(INPUT_VIDEO, EXTRACTED_AUDIO)
segments = list(transcribe_audio(EXTRACTED_AUDIO))

for s in segments:
    s["text"] = improve_text(s["text"])

create_srt(segments, OUTPUT_SRT)

apply_subtitle(INPUT_VIDEO, OUTPUT_SRT, OUTPUT_VIDEO)

print("Legendas geradas e aplicadas com sucesso!")
