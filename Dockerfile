FROM python:3.11

RUN apt-get update && apt-get install -y ffmpeg

RUN pip install streamlit hf_xet ffmpeg pydub requests python-dotenv groq libass

WORKDIR /app

COPY . /app

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
