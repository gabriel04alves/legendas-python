import streamlit as st
import re
import yt_dlp
import os


def download_video(url, output_dir):
    fonts = {
        "youtube": r"(youtube\.com|youtu\.be)",
        "instagram": r"instagram\.com",
        "facebook": r"facebook\.com",
        "twitter": r"(twitter\.com|x\.com)",
        "tiktok": r"tiktok\.com",
    }

    for name, pattern in fonts.items():
        if re.search(pattern, url):
            st.write(f"Baixando vídeo de {name}...")
            output_path = os.path.join(output_dir, "downloaded_video.mp4")

            ydl_opts = {
                "format": "best[ext=mp4]/best",
                "outtmpl": output_path,
                "quiet": True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            return {
                "path": output_path,
                "name": "downloaded_video.mp4",
                "read": lambda: open(output_path, "rb").read(),
            }

    st.error("Plataforma não suportada.")
    return None
