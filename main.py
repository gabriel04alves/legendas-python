from app.audio_processing import extract_audio
from app.transcription import transcribe_audio
from app.text_improve import improve_text
from app.format_srt_time import format_srt_time
from app.srt_create import create_srt

INPUT_VIDEO = "/app/video.mp4"
EXTRACTED_AUDIO = "/app/audio.mp3"
OUTPUT_SRT = "/app/legendas.srt"

extract_audio(INPUT_VIDEO, EXTRACTED_AUDIO)
segments = transcribe_audio(EXTRACTED_AUDIO)

caption_text = "\n".join(
    f"{format_srt_time(s.start)} --> {format_srt_time(s.end)}\n{s.text.strip()}"
    for s in segments
)

improved = improve_text(caption_text)

create_srt(improved, OUTPUT_SRT)

print("✔ Legendas geradas com sucesso!")
