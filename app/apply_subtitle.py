import subprocess


def apply_subtitle(video_path, subtitle_path, output_path):
    command = [
        "ffmpeg",
        "-i",
        video_path,
        "-vf",
        f"subtitles={subtitle_path}:force_style='Fontsize=15'",
        "-c:a",
        "copy",
        output_path,
    ]

    subprocess.run(command, check=True)
