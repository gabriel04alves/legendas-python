from faster_whisper import WhisperModel
from pydub import AudioSegment

name_file = "video.mp4"
file_location = f"/app/{name_file}"
type_file = name_file.split(".")[1]

audio_file = AudioSegment.from_file(file_location, format=type_file)
audio_file.export("/app/audio.mp3", format="mp3")

model = WhisperModel("medium", compute_type="int8")

segments, _ = model.transcribe("/app/audio.mp3", language="pt")

translated = " ".join([segment.text for segment in segments])

print(translated)
