FROM python:3.11

RUN apt-get update && apt-get install -y ffmpeg

RUN pip install faster-whisper ffmpeg pydub

WORKDIR /app

COPY . /app

CMD ["python", "main.py"]
