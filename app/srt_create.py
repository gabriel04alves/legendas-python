from app.format_srt_time import format_srt_time


def create_srt(segments, output_path="legendas.srt"):
    with open(output_path, "w", encoding="utf-8") as file:
        for i, segment in enumerate(segments, 1):
            start = format_srt_time(segment["start"])
            end = format_srt_time(segment["end"])
            text = segment["text"].strip()

            file.write(f"{i}\n")
            file.write(f"{start} --> {end}\n")
            file.write(f"{text}\n\n")
