# text_to_audio_speaker
Reads a text provided and reproduces in audio

Implements:
- gTTS (Google Text-to-Speech) Python library https://gtts.readthedocs.io/en/latest/
- Streamlit in Python to user interface

Steps:

1) run a docker image
   $ docker container run -d -p 8501:8501 python:3.10 sleep infinity
   
2) pip install -r requirements.txt

3) streamlit run main.py