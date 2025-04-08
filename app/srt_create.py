from app.format_srt_time import format_srt_time


def create_srt(text, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)
