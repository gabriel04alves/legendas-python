from faster_whisper import WhisperModel


def transcribe_audio(audio_path):
    model = WhisperModel("medium", compute_type="int8")
    segments, _ = model.transcribe(audio_path, language="pt")
    return list(segments)
