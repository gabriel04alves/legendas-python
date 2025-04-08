from pydub import AudioSegment


def extract_audio(input_path, output_path):
    file_type = input_path.split(".")[-1]
    audio = AudioSegment.from_file(input_path, format=file_type)
    audio.export(output_path, format="mp3")
