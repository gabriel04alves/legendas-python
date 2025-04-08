FROM python:3.11

RUN apt-get update && apt-get install -y ffmpeg

RUN pip install hf_xet ffmpeg pydub requests python-dotenv groq

WORKDIR /app

COPY . /app

CMD ["python", "main.py"]
